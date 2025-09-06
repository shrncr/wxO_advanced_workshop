# wxO Advanced workshop AI Gateway lab
## What you will learn
In this lab you will learn a number of concepts including:
- **Connections:** Automating the import of connections. 
    - Create a connection to establish the App ID `--app-id` which is the name of the connection.
    - Setting the connection's environment, type, and flags
    - Setting the connection's credentials.
    - A yaml style connection which is best for wxO devops workflows with both `draft` and `live` environments.
- **Models:** Automating the import of external models for **native agent** use! This extends the already large built-in library of LLM's that come with wxO to include any external LLM that your customer is already using. 
    - Importing OpenAI models, like `GPT 4.1 mini`
    - Importing Google models, like `Gemini 2.5 Flash`
    - Importing Claude models, like `Opus 4`
- **Agents:** Using agents as supervisors to delegate tasks to collaborator agents. 
    - Defining agents with yaml to make them easy to load. Way faster than the UI! 
    - How wxO makes it easy to create an agentic pattern called LLM as judge.

## Getting started

Follow these steps for the lab.

Step 1: [README_for_connections.md](src/connections/README_for_connections.md "Go to Step 1 now")

Step 2: [README_for_models.md](src/models/README_for_models.md "Go to Step 2 now")

Step 3: [README_for_agents.md](src/agents/README_for_agents.md "Go to Step 3")

Step 4: Having some fun time! Try these prompts with your Claude as Judge agent


```bash
orchestrate chat start
```

Let's prime each agent to make sure they are connecting properly.

- Try the OpenAI agent with a prompt of `hello` to get it primed.
- Try the Gemini agent with a prompt of `hello` to get it primed.

- Now try the Claude as Judge with this prompt:
```
Write a 5 sentence story about Daniel, the sailboat skipper, adventuring in the Caribbean ocean.
```
If the agent hangs or times out. Click to another agent in the drop down then click back and try again. 

Congratulations! You've completed the AI Gateway lab.

## Using AI Gateway in SaaS instances

This feature works locally and is already implemented in production for IBM Cloud SaaS instances ***(AWS instances?? - get answer for that)***. That means all you have to do is point your orchestrate ADK to your SaaS environment `orchestrate env activate <my_aws_wxo>` and then import the connections, models, and agents for this lab to have it working on the SaaS instances too! That is a giant advantage to watsonx Orchestrate to have this level of native agent support for any vendor's LLMs. 

Here are some other things to keep in mind as you [implement AI Gateway](https://connect.watson-orchestrate.ibm.com/acf/gateway/implementation-considerations) for your projects. 


## Cleaning up

`NOTE:` Don't do this until the end of the workshop. 

It's a good idea to learn how to clean up your work from an environment via the ADK CLI commands. You should do them in this particular order, which is just the opposite of the import order. The reason is that if you stopped half way,let's say you removed the agents but wanted to test something that needed the models and connections to be present you still can. Also, it's the dependency order of agents need models need connection, so nothing gets out of sync in your environment with you or other collaborators trying to use those resources as you are removing them. 

### Remove agents first


When you want to remove the agents keep in mind that:
- ✅ The best practice is to ***remove the agents with collaborators*** first, so you don't inadvertently try to use it and the collaborators are already gone. 
- 🧨 The `--name` flag requires the name defined in the yaml file ```yaml
name: OpenAI_agent``` NOT the file name.

```bash
orchestrate agents remove -k native --name Claude_as_Judge

orchestrate agents remove -k native --name Gemini_2_agent

orchestrate agents remove -k native --name OpenAI_agent
```

### Remove models second

`NOTE:` Don't do this until the end of the workshop.

The `--name` flag is all that is needed to remove the model but you need to know the name of the model so `orchestrate model list` is a fast way to check the model names.

```bash
orchestrate models remove --name virtual-model/anthropic/claude-opus-4-20250514

orchestrate models remove --name virtual-model/google/gemini-2.5-flash 

orchestrate models remove --name virtual-model/openai/gpt-4.1-mini 
```

### Remove connection third 

```bash
orchestrate connections remove --app-id openai_creds

orchestrate connections remove --app-id gemini_creds

orchestrate connections remove --app-id claude_creds
```

And that's it!

## Congratulations you have finished the ai-gateway-lab!