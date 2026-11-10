#!/usr/bin/env bash
# Usage: ./scripts/push-to-github.sh [repo-name]
set -euo pipefail

USER_NAME="farhanmugdho"
REPO="${1:-docker-compose-multi-container}"

[ -d .git ] || git init -b main
git add .
git commit -m "Multi-container app: Nginx + Flask + PostgreSQL with Docker Compose" || echo "Nothing new to commit"

if command -v gh >/dev/null 2>&1; then
  # GitHub CLI route (creates repo and pushes in one go)
  gh repo create "$USER_NAME/$REPO" --public --source=. --remote=origin --push \
    || { git remote add origin "https://github.com/$USER_NAME/$REPO.git" 2>/dev/null || true; git push -u origin main; }
else
  # Plain git route (create an empty repo on github.com first)
  git remote add origin "https://github.com/$USER_NAME/$REPO.git" 2>/dev/null || true
  git push -u origin main
fi

echo "Done: https://github.com/$USER_NAME/$REPO"
