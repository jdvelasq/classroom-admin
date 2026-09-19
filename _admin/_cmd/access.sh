#!/usr/bin/env bash
# Usage: ./add_collaborator.sh <ORG> <REPO_NAME> <COLLABORATOR_USERNAME>
# Example: ./add_collaborator.sh my-org hw01-alice outsider-username

set -euo pipefail

if [ "$#" -ne 4 ]; then
  echo "Usage: $0 <ORG> <REPO_NAME> <COLLABORATOR_USERNAME> <TEMPLATE>" >&2
  exit 1
fi

ORG="$1"
REPO="$2"
COLLABORATOR="$3"
TEMPLATE="$4"

# Ensure gh is installed and authed
if ! command -v gh >/dev/null 2>&1; then
  echo "Error: GitHub CLI (gh) is not installed." >&2
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "Error: gh is not authenticated. Run: gh auth login" >&2
  exit 1
fi

ORG_REPO="${ORG}/${REPO}"
ORG_TEMPLATE="${ORG}/${TEMPLATE}"

# If repo exists, delete and create again
# if gh repo view "$ORG_REPO" >/dev/null 2>&1; then
#   gh repo delete "$ORG_REPO" --yes
#   gh repo create "$ORG_REPO" --public --template "$ORG_TEMPLATE" -y 
# fi

# Add collaborator with write (push) access
gh api \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  "/repos/${ORG_REPO}/collaborators/${COLLABORATOR}" \
  -f permission=push \
  >/dev/null 2>&1


echo "  ${ORG_REPO}"