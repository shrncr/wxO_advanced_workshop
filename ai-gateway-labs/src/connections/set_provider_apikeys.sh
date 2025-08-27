#!/bin/bash
# Lab proctor will provide the API keys for Claude, Gemini, and OpenAI.
# This script sets the API keys as environment variables.

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "Script directory: $SCRIPT_DIR"

# Function to check if all API keys exist and are not blank
check_all_keys_exist() {
    [ -n "$CLAUDE_API_KEY" ] && [ -n "$GEMINI_API_KEY" ] && [ -n "$OPENAI_API_KEY" ]
}

# Function to display current API keys (masked for security)
display_current_keys() {
    echo "Current API Keys:"
    echo "  Claude API Key: ${CLAUDE_API_KEY:0:10}...${CLAUDE_API_KEY: -4}"
    echo "  Gemini API Key: ${GEMINI_API_KEY:0:10}...${GEMINI_API_KEY: -4}"
    echo "  OpenAI API Key: ${OPENAI_API_KEY:0:10}...${OPENAI_API_KEY: -4}"
}

# Function to prompt for API key with current value check
prompt_for_key() {
    local key_name=$1
    local key_var=$2
    local current_value=${!key_var}
    
    if [ -n "$current_value" ]; then
        echo "Current $key_name: ${current_value:0:10}...${current_value: -4}"
        read -p "Keep this value? (y/n): " confirm
        if [[ $confirm == "y" || $confirm == "Y" ]]; then
            return 0  # Keep current value
        fi
    fi
    
    read -p "Enter $key_name: " new_value
    export $key_var="$new_value"
}

echo "=== API Key Setup ==="

# Check if all API keys already exist and are not blank
if check_all_keys_exist; then
    echo "All API keys are already set in environment variables."
    echo ""
    display_current_keys
    echo ""
    read -p "Are these API key values correct? (y/n): " confirm_all
    
    if [[ $confirm_all == "y" || $confirm_all == "Y" ]]; then
        echo "Using existing API keys from environment variables."
    else
        echo "Please update the API keys:"
        echo ""
        # Re-prompt for all keys
        prompt_for_key "Claude API Key" "CLAUDE_API_KEY"
        prompt_for_key "Gemini API Key" "GEMINI_API_KEY"
        prompt_for_key "OpenAI API Key" "OPENAI_API_KEY"
    fi
else
    echo "Setting up API keys (some may be missing or empty)..."
    echo ""
    # Check and set each key individually
    prompt_for_key "Claude API Key" "CLAUDE_API_KEY"
    prompt_for_key "Gemini API Key" "GEMINI_API_KEY"
    prompt_for_key "OpenAI API Key" "OPENAI_API_KEY"
fi

echo ""
echo "Final API Key Status:"
echo "  CLAUDE_API_KEY: ${CLAUDE_API_KEY:+SET}${CLAUDE_API_KEY:-NOT SET}"
echo "  GEMINI_API_KEY: ${GEMINI_API_KEY:+SET}${GEMINI_API_KEY:-NOT SET}"
echo "  OPENAI_API_KEY: ${OPENAI_API_KEY:+SET}${OPENAI_API_KEY:-NOT SET}"

echo ""
echo "API keys have been set as environment variables."
echo ""

# Run the connection shell scripts to complete the connections setup.
echo "=== Running Connection Scripts ==="

if [ -f "$SCRIPT_DIR/claude.sh" ]; then
    echo "Running claude.sh..."
    bash "$SCRIPT_DIR/claude.sh" 2>&1
    echo "Claude connection script completed."
else
    echo "Warning: claude.sh not found in $SCRIPT_DIR"
fi

echo ""

if [ -f "$SCRIPT_DIR/gemini.sh" ]; then
    echo "Running gemini.sh..."
    bash "$SCRIPT_DIR/gemini.sh" 2>&1
    echo "Gemini connection script completed."
else
    echo "Warning: gemini.sh not found in $SCRIPT_DIR"
fi

echo ""

if [ -f "$SCRIPT_DIR/openai.sh" ]; then
    echo "Running openai.sh..."
    bash "$SCRIPT_DIR/openai.sh" 2>&1
    echo "OpenAI connection script completed."
else
    echo "Warning: openai.sh not found in $SCRIPT_DIR"
fi

echo ""
echo "All connection scripts have been executed!"