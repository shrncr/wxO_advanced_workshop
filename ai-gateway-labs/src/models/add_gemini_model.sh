#!/bin/bash
# This script adds the Gemini Pro model via the Orchestrate CLI.

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

# Add Gemini 2.5 Flash model
# Note: This model import method does not support --tags (which the yaml method does)
orchestrate models add \
--name google/gemini-2.5-flash \
--app-id gemini_creds \
--type chat \
--description "Gemini 2.5 Flash model" \
--display-name "Gemini 2.5 Flash" \
--provider-config '{"request_timeout": 20000}'