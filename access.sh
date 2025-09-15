#!/usr/bin/env bash
# Usage: ./add_collaborator.sh <ORG> <REPO_NAME> <COLLABORATOR_USERNAME>
# Example: ./add_collaborator.sh my-org hw01-alice outsider-username

set -euo pipefail

if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <ORG> <REPO_NAME> <COLLABORATOR_USERNAME>" >&2
  exit 1
fi

ORG="$1"
REPO="$2"
COLLABORATOR="$3"

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


# Remove collaborator if exists
gh api \
  -X DELETE \
  -H "Accept: application/vnd.github+json" \
  "/repos/${ORG_REPO}/collaborators/${COLLABORATOR}" \
  >/dev/null 2>&1 || true

# Add collaborator with write (push) access
gh api \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  "/repos/${ORG_REPO}/collaborators/${COLLABORATOR}" \
  -f permission=push \
  >/dev/null 2>&1


echo "  ${ORG_REPO}"