#!/bin/bash
# Lab proctor will provide the API keys for Claude, Gemini, and OpenAI.
# This script sets the API keys as environment variables.
# Prompt user for API keys
read -p "Enter Claude API Key: " claude_key
read -p "Enter Gemini API Key: " gemini_key
read -p "Enter OpenAI API Key: " openai_key

# Export as environment variables
export CLAUDE_API_KEY="$claude_key"
echo "CLAUDE_API_KEY= $CLAUDE_API_KEY"
export GEMINI_API_KEY="$gemini_key"
echo "GEMINI_API_KEY= $GEMINI_API_KEY"
export OPENAI_API_KEY="$openai_key"
echo "OPENAI_API_KEY= $OPENAI_API_KEY"

echo "API keys have been set as environment variables."

# Run the connections shell scripts to complete the connections setup.
./src/connections/claude.sh
./src/connections/gemini.sh
./src/connections/openai.sh

echo "All connections imported successfully!"