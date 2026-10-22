#!/usr/bin/env python3
"""Compare prescribed instruction reads; does not measure model execution cost."""
from __future__ import annotations

import argparse
from functools import cache
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_skill import EXPECTED_MODELS, ROUTING_GUIDES


def measure(root: Path) -> dict:
    baseline = json.loads((root / 'docs/evaluation/baseline-files.json').read_text())

    @cache
    def file_size(path: str) -> tuple[int, int]:
        data = (root / path).read_bytes()
        return len(data.decode("utf-8").split()), len(data)

    def current(paths: list[str]) -> dict:
        return {'words': sum(file_size(p)[0] for p in paths),
                'bytes': sum(file_size(p)[1] for p in paths),
                'reads': len(paths)}

    def previous(paths: list[str]) -> dict:
        return {'words': sum(baseline[p]['words'] for p in paths),
                'bytes': sum(baseline[p]['bytes'] for p in paths),
                'reads': len(paths)}

    rows = []
    for filename, (title, category) in EXPECTED_MODELS.items():
        card = f'references/{filename}'
        old_paths = ['SKILL.md', 'references/catalog.md', card]
        for mode, new_paths in [
            ('named', ['SKILL.md', 'references/catalog.md', card]),
            ('automatic', ['SKILL.md', 'references/selection.md',
                           f'references/{ROUTING_GUIDES[category]}', card]),
        ]:
            rows.append({'model': title, 'mode': mode, 'before': previous(old_paths),
                         'after': current(new_paths), 'after_paths': new_paths})
    for reference in ['formal-validity.md', 'induction.md']:
        paths = ['SKILL.md', 'logic/overview.md', f'logic/{reference}', 'logic/fallacies.md']
        rows.append({'model': f'/logic with {reference}', 'mode': 'logic',
                     'before': previous(paths), 'after': current(paths), 'after_paths': paths})
    changed = [p for p, value in baseline.items()
               if p not in {'SKILL.md', 'references/catalog.md'}
               and hashlib.sha256((root / p).read_bytes()).hexdigest() != value['sha256']]
    return {'metric': 'static UTF-8 bytes, whitespace words, logical file reads',
            'limitations': 'No model usage tokens, latency, retries, cache accounting or quality inferred.',
            'changed_cards_or_logic': changed, 'routes': rows}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    result = measure(args.root.resolve())
    print(json.dumps(result, indent=2))
    return int(bool(result['changed_cards_or_logic']))


if __name__ == '__main__':
    raise SystemExit(main())
