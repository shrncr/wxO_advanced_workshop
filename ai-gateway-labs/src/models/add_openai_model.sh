#!/bin/bash
# This script adds the OpenAI model to your watsonx Orchestrate environment.

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

# Add OpenAI GPT-4.1-mini model
# Note: This model import method does not support --tags (which the yaml method does)
orchestrate models add \
--name openai/gpt-4.1-mini \
--app-id openai_creds \
--type chat \
--description "OpenAI GPT 4.1 mini" \
--display-name "GPT 4.1 mini" \
--provider-config '{"request_timeout": 20000}'