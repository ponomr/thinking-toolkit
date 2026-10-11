"""Regression checks for the explicitly invoked toolkit metadata contract."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("policy_validator", ROOT / "scripts" / "validate_skill.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

class ExplicitPolicyTests(unittest.TestCase):
    def test_policy_contract(self):
        base = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
        cases = [
            ("correct", base, False),
            ("enabled", base.replace("allow_implicit_invocation: false", "allow_implicit_invocation: true"), True),
            ("missing", base.split("policy:")[0], True),
            ("quoted", base.replace("allow_implicit_invocation: false", 'allow_implicit_invocation: "false"'), True),
            ("duplicate", base + "policy:\n  allow_implicit_invocation: false\n", True),
            ("wrong-interface", base.replace("display_name:", "other_name:"), True),
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "openai.yaml"
            for name, text, reject in cases:
                with self.subTest(case=name):
                    path.write_text(text, encoding="utf-8")
                    self.assertEqual(bool(validator.validate_agent_metadata(path)), reject)

if __name__ == "__main__":
    unittest.main()
