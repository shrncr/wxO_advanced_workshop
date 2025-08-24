# Step 3: Load the agents

## Setup
🚨 Do this step AFTER you have added the connections

🚨 Do this AFTER you have added the models

---

🚀 Now, let's use the yaml import method to get the agents loaded. This is way faster than creating agents via the UI and allows for more control of the agent's attributes. 

🧨 The order that we load these agents is important because agents with collaborator agents defined will not load until the collaborator agents are available. For example, the `llm_as_judge.yaml` agent wants two collaborator agents which are defined in the `gemini_2_agent.yaml` and the `openai_agent.yaml` files so it has to be the last one we import. 🤓

```bash
orchestrate agents import --file src/agents/gemini_2_agent.yaml

orchestrate agents import --file src/agents/openai_agent.yaml

orchestrate agents import --file src/agents/llm_as_judge.yaml
```

## Cleanup

When you want to remove the agents keep in mind that:
- ✅ The best practice is to ***remove the agents with collaborators*** first, so you don't inadvertently try to use it and the collaborators are already gone. 
- 🧨 The `--name` flag requires the name defined in the yaml file ```yaml
name: OpenAI_agent``` NOT the file name.

```bash
orchestrate agents import -k native --name Claude_as_Judge

orchestrate agents remove -k native --name Gemini_2_agent

orchestrate agents import -k native --name OpenAI_agent
```