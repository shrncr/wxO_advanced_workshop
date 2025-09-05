# Step 2: Load the models

## Setup
 
There are two ways to get models into watsonx Orchestrate via the ADK
Let's use the first method because it allows for precise control of the imported model's attributes. Additionally, unlike the orchestrate models add command it allows the use of tags that will help your model to be easily identified in the UI like this:

![Model tags in UI](../../resources/model_tags.png)

Note that the `--app-id` is **required** when you add models with a yaml file. So do this **AFTER** you add the connections which set the `--app-id` you need.

```bash
orchestrate models import --file src/models/claude.yaml --app-id claude_creds

orchestrate models import --file src/models/gemini.yaml --app-id gemini_creds

orchestrate models import --file src/models/openai.yaml --app-id openai_creds

```

You have completed Step 2 of the lab.

Please proceed to [Step 3](../agents/README_for_agents.md) of the lab

