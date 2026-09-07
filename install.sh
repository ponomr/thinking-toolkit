#!/usr/bin/env bash
# Install the thinking-toolkit skill into a host agent's skills directory.
#
# Usage: ./install.sh [--force] [claude|codex|openclaw|all|<path>]
#
#   --force     Replace an existing install without asking. The prior version
#               is preserved as a sibling backup.
#   target      Which agent to install for (default: all detected agents).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Only the skill payload and its explicit updater are installed. Repository
# docs, tests, validation tooling, and release tooling stay out.
PAYLOAD=(SKILL.md references logic agents LICENSE VERSION update.py)

FORCE="no"
TARGET=""

for arg in "$@"; do
  case "$arg" in
    --force)   FORCE="yes" ;;
    --help|-h) grep '^#' "$0" | sed 's/^# \{0,1\}//' | head -8; exit 0 ;;
    -*)        echo "unknown option: $arg" >&2; exit 2 ;;
    *)         TARGET="$arg" ;;
  esac
done
TARGET="${TARGET:-all}"

install_to() {
  local dest="$1/thinking-toolkit"
  local backup=""
  local suffix=""

  if [ -e "$dest" ] || [ -L "$dest" ]; then
    if [ "$FORCE" = "yes" ]; then
      backup="${dest}.backup.$(date +%Y%m%d%H%M%S).$$"
      while [ -e "$backup" ] || [ -L "$backup" ]; do
        suffix="${suffix}x"
        backup="${dest}.backup.$(date +%Y%m%d%H%M%S).$$.${suffix}"
      done
      mv "$dest" "$backup"
    elif [ -t 0 ]; then
      printf 'exists   -> %s\n         overwrite? [y/N] ' "$dest"
      read -r reply
      case "$reply" in
        [yY]*)
          backup="${dest}.backup.$(date +%Y%m%d%H%M%S).$$"
          while [ -e "$backup" ] || [ -L "$backup" ]; do
            suffix="${suffix}x"
            backup="${dest}.backup.$(date +%Y%m%d%H%M%S).$$.${suffix}"
          done
          mv "$dest" "$backup"
          ;;
        *) echo "skipped  -> $dest"; return ;;
      esac
    else
      echo "skipped  -> $dest (already exists; pass --force to overwrite)"
      return
    fi
  fi

  mkdir -p "$1"
  if ! mkdir -p "$dest"; then
    [ -n "$backup" ] && mv "$backup" "$dest"
    return 1
  fi
  for item in "${PAYLOAD[@]}"; do
    if ! cp -R "${SCRIPT_DIR}/${item}" "$dest/"; then
      rm -rf "$dest"
      [ -n "$backup" ] && mv "$backup" "$dest"
      return 1
    fi
  done
  echo "copied   -> $dest"
  [ -n "$backup" ] && echo "backup   -> $backup"
}

case "$TARGET" in
  claude)   install_to "${HOME}/.claude/skills" ;;
  codex)    install_to "${HOME}/.codex/skills" ;;
  openclaw) install_to "${HOME}/.openclaw/skills" ;;
  all)
    for dir in "${HOME}/.claude/skills" "${HOME}/.codex/skills" "${HOME}/.openclaw/skills"; do
      parent="$(dirname "$dir")"
      # Install only for agents that are actually present on this machine.
      [ -d "$parent" ] && install_to "$dir" || echo "skipped  -> $dir (no $(basename "$parent") setup)"
    done
    ;;
  *) install_to "$TARGET" ;;
esac
