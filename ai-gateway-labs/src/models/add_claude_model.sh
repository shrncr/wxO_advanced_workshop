#!/bin/bash
# This script adds the Claude Sonnet 4 model to the Orchestrate CLI.

# Error handling
# Exit on error
set -e

# Exit if any command fails
exit_on_failure() {
    if [ $? -ne 0 ]; then
        echo "Error: An error occurred in the script."
        exit 1
    fi
}

# Target the watsonx Orchestrate local environment
orchestrate env activate local

# Add Anthropic Claude Opus model
# Note: This model import method does not support --tags (which the yaml method does)
orchestrate models add \
--name anthropic/claude-opus-4-20250514 \
--app-id claude_creds \
--type chat \
--description "Anthropic Claude Sonnet 4 model" \
--display-name "Claude Sonnet 4" \
--provider-config '{"request_timeout": 20000}'