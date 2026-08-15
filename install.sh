#!/usr/bin/env bash
# Install the thinking-toolkit skill into a host agent's skills directory.
#
# Usage: ./install.sh [--symlink] [--force] [claude|codex|openclaw|all|<path>]
#
#   --symlink   Link the skill instead of copying it, so `git pull` in this
#               repo updates every install at once.
#   --force     Overwrite an existing install without asking.
#   target      Which agent to install for (default: all detected agents).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# Only the skill payload is installed; repo docs, tests, and tooling stay out.
PAYLOAD=(SKILL.md references logic agents)

MODE="copy"
FORCE="no"
TARGET=""

for arg in "$@"; do
  case "$arg" in
    --symlink) MODE="symlink" ;;
    --force)   FORCE="yes" ;;
    --help|-h) grep '^#' "$0" | sed 's/^# \{0,1\}//' | head -8; exit 0 ;;
    -*)        echo "unknown option: $arg" >&2; exit 2 ;;
    *)         TARGET="$arg" ;;
  esac
done
TARGET="${TARGET:-all}"

install_to() {
  local dest="$1/thinking-toolkit"

  if [ -e "$dest" ] || [ -L "$dest" ]; then
    if [ "$FORCE" = "yes" ]; then
      rm -rf "$dest"
    elif [ -t 0 ]; then
      printf 'exists   -> %s\n         overwrite? [y/N] ' "$dest"
      read -r reply
      case "$reply" in [yY]*) rm -rf "$dest" ;; *) echo "skipped  -> $dest"; return ;; esac
    else
      echo "skipped  -> $dest (already exists; pass --force to overwrite)"
      return
    fi
  fi

  mkdir -p "$1"
  if [ "$MODE" = "symlink" ]; then
    mkdir -p "$dest"
    for item in "${PAYLOAD[@]}"; do
      ln -s "${SCRIPT_DIR}/${item}" "${dest}/${item}"
    done
    echo "linked   -> $dest"
  else
    mkdir -p "$dest"
    for item in "${PAYLOAD[@]}"; do
      cp -R "${SCRIPT_DIR}/${item}" "$dest/"
    done
    echo "copied   -> $dest"
  fi
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
