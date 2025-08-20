#!/bin/bash
set -e
# This script sets up the agent environment and installs necessary dependencies.

# Resolve the directory where this script lives
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Import web search tool (paths are now relative to the script location)
orchestrate tools import \
  -k python \
  -f "$SCRIPT_DIR/tools/web_search_tool/web_search.py" \
  -r "$SCRIPT_DIR/tools/web_search_tool/requirements.txt" \
  --app-id tavily

# Import agent
orchestrate agents import \
  -f "$SCRIPT_DIR/agents/agent.yaml"

