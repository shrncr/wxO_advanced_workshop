# wxO Advanced workshop AI Gateway lab
## What you will learn
In this lab you will learn a number of concepts including:
- **Connections:** Automating the import of connections. 
    - Create the connection to establishe the App ID `--app-id` which is the name of the connection.
    - Setting the connection's environment, type, and flags
    - Setting the connection's credentials.
    - A yaml style connection which is best for SaaS environments with both `draft` and `live` environments.
- **Models:** Automating the import of external models for **native agent** use!
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
write a 5 sentence story about Daniel the sailboat skippers adventures in the Caribbean ocean.
```
If the agent hangs or times out. Click to another agent in the drop down then click back and try again. 

Congratulations! You've completed the AI Gateway lab.

## Using AI Gateway in SaaS instances

This feature works locally and is already implemented in production for IBM Cloud SaaS instances ***(AWS instances?? - get answer for that)***. That means all you have to do is point your orchestrate ADK to your SaaS environment `orchestrate env activate <my_ibmcloud_wxo>` and then import the connections, models, and agents for this lab to have it working on the SaaS instances too! That is a giant advantage to watsonx Orchestrate to have this level of native agent support for any vendor's LLM. 

Here are some other things to keep in mind as you [implement AI Gateway](https://connect.watson-orchestrate.ibm.com/acf/gateway/implementation-considerations) for your projects. 


## Cleaning up

Each README file in `connections` `models` and `agents` folder has a section called **Cleanup** that will help you to remove the lab assets from your environment. You should to them in this order, which is just the opposite of the import order. The reason is that if you stopped half way,let's say you removed the agents but wanted to test something that needed the models and connections to be present you still can. Also, it's the dependency order of agents need models need connection, so nothing gets out of sync in your environment with you or other collaborators trying to use those resources as you are removing them. 

- Remove agents first with the [cleanup agents steps](src/agents/README_for_agents.md#cleanup)
- Remove models second with the [cleanup models steps](src/models/README_for_models.md#cleanup)
- Remove connection third with the [cleanup connections steps](src/connections/README_for_connections.md#cleanup)