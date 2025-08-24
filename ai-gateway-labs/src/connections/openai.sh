#!/bin/bash
# This script sets up a connection for OpenAI credentials.

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

# Assign an App ID to the connection
orchestrate connections add -a openai_creds
# Configure the connection for the draft environment
orchestrate connections configure -a openai_creds --env draft -k key_value -t team
# Set the credentials for the draft environment
orchestrate connections set-credentials -a openai_creds --env draft -e "api_key=$OPENAI_API_KEY"

## Live environement setup (uncomment for SaaS deployment) ### ADK only supports draft env configurations

# Set the credentials for the live environment
# orchestrate connections configure -a openai_creds --env live -k key_value -t team
# Set the credentials for the live environment
# orchestrate connections set-credentials -a openai_creds --env live -e "api_key=$OPENAI_API_KEY"