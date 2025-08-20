#!/usr/bin/env bash
set -euo pipefail

# ========================================================
# Langfuse Orchestration Setup Script
# ========================================================
# This script configures observability settings for Langfuse.
# It expects a `.env` file with the following variables:
#   LANGFUSE_PROJECT_ID=<your-project-id>
#   LANGFUSE_API_KEY=<your-api-key>
# ========================================================

# Load environment variables from .env file
if [[ -f .env ]]; then
  export $(grep -v '^#' .env | xargs)
else
  echo " .env file not found. Please create one with required variables."
  exit 1
fi

# Validate required environment variables
if [[ -z "${LANGFUSE_PROJECT_ID:-}" || -z "${LANGFUSE_API_KEY:-}" ]]; then
  echo " Missing LANGFUSE_PROJECT_ID or LANGFUSE_API_KEY in .env file."
  exit 1
fi

# Run Langfuse configuration
echo "Configuring Langfuse observability..."
orchestrate settings observability langfuse configure \
  --url "https://us.cloud.langfuse.com/api/public/otel" \
  --health-uri "https://us.cloud.langfuse.com" \
  --project-id "$LANGFUSE_PROJECT_ID" \
  --api-key "$LANGFUSE_API_KEY"

echo "Langfuse observability configured successfully."
