#!/usr/bin/env bash
# Create the student repo from template
# Usage: ./create_repo_from_template.sh <ORG> <REPO_NAME> <TEMPLATE_OWNER/TEMPLATE_REPO>
# Example: ./create_repo_from_template.sh my-org hw01-alice my-org/starter-hw01

set -euo pipefail

if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <ORG> <REPO_NAME> <TEMPLATE_OWNER/TEMPLATE_REPO>" >&2
  exit 1
fi

ORG="$1"
REPO="$2"
TEMPLATE="$3"

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

# If repo already exists, exit cleanly (idempotent behavior)
if gh repo view "$ORG_REPO" >/dev/null 2>&1; then
  echo "   Exists: ${ORG_REPO}"
  exit 0
fi

# Create repo from template (private by default). Add --public if you want.
if gh repo create "$ORG_REPO" --public --template "$ORG_TEMPLATE" -y >/dev/null 2>&1; then
  echo "  Created: ${ORG_REPO}"
else
  echo "     Fail: ${ORG_REPO}"
  exit 1
fi
