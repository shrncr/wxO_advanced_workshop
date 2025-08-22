# Multi-Agent Labs
## Context Variables 
### Setting Agent `context_variables` from Tool output

#### Learning objectives:
- Experience how an agents and tools pass data to each other.
- Built-in `context_varibles` that watsonx Orchestrate provides.
- Defining your own custom context_variables.
- Setting your custom context_variables with Tool output. 

### 1. Setup your ADK local environment:
- Import the "context variables" agent with the **context_variable_tool.py** and **requirements.txt** files.

`orchestrate tools import -k python -f multi-agent-labs/lab-01/src/tools/make_uppercase.py -r multi-agent-labs/lab-01/src/tools/requirements.txt`

- Import the "context_variables_tool" with the **context_variables.yaml** file.

`orchestrate agents import -f multi-agent-labs/lab-01/src/agents/context_variables.yaml`

### 2. Test the context_variables agent in the ADK local chat

### 3. Modify the tool's return code and observe changes.
```
# Modify the existing return statement to look like this:
return merged_data
```
Reimport the agents and tools and observe how the agent responds to the prompt now.

Revert your changes to the tool and import it again to prepare for the next step.

### 4. Modify the agent's instructions and observe changes.

```
# Modify the instructions element to look like this:


```


### x. Clean up your ADK local environment:
- Remove the "context variables" agent.

`orchestrate tools remove -k python -n context_variables`

- Remove the "context_variables_tool" tool.

`orchestrate tools remove -n context_variables_tool`