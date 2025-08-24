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

Step 1: [README for connections.md](src/connections/README for connections.md "Go to Step 1")

Step 2: [README for models.md](src/models/README for models.md "Go to Step 2")

Step 3: [README for agents.md](src/agents/README for agents.md "Go to Step 3")

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

## Cleaning up

Each README file in `connections` `models` and `agents` folder has a section called **Cleanup** that will help you to remove the lab assets from your environment. You should to them in this order.

- Remove agents first
- Remove models second
- Remove connection third