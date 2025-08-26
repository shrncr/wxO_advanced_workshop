# GitHub MCP Lab
#### [Made by sophia southard with Scribe](https://scribehow.com/shared/GitHub_MCP_Lab__pemXOUvzTTCFbCPy9gF_1g)
This lab demonstrates how watsonx Orchestrate can integrate with developer tools like GitHub using the Model Context Protocol (MCP). You’ll see how to connect GitHub securely, import its toolkit, and build an AI agent that can interact with GitHub in plain language. 

References for this lab: https://heidloff.net/article/orchestrate-mcp/

#### Create GitHub Personal Access Token (PAT)


Tip: This token will allow us to have the correct scopes for the GitHub MCP Server


1\. Login to your GitHub account & Navigate to "Settings"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/434deaf3-3af1-4289-a9c8-a48c4ede7b68/ascreenshot.jpeg?tl_px=94,85&br_px=1470,854&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=808,277)


2\. Navigate to & Click "Developer settings"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/a2051897-f444-4b42-a3de-597490986a66/ascreenshot.jpeg?tl_px=0,186&br_px=1376,956&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=192,448)


3\. Click "Personal access tokens"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/3b447bce-a358-4caf-b42f-20b5989d6e77/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=210,174)


4\. Click "Tokens (classic)"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/6d64c59f-b6b4-4e1c-b247-37f94dd670f8/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=181,225)


5\. Click "Generate new token **(classic)**"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/9d82cc27-434f-4df2-8e64-91b748a9f012/ascreenshot.jpeg?tl_px=74,80&br_px=1451,849&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=524,277)


6\. Click "repo Full control of private repositories"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/3687576f-1c3f-42ef-937b-f2ee82081a68/ascreenshot.jpeg?tl_px=0,164&br_px=1376,933&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=322,277)


7\. Click "admin:org Full control of orgs and teams, read and write org projects"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/84cfd384-2736-4a64-8b6d-4c321b3eb082/ascreenshot.jpeg?tl_px=0,186&br_px=1376,956&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=324,429)


8\. Click "Generate token"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/212ed54d-a499-4813-b65c-864de696b703/ascreenshot.jpeg?tl_px=0,186&br_px=1376,956&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=349,384)


9\. **COPY YOUR TOKEN**, you will not be able to see it again

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/4f54cd35-8719-4ad7-b710-c5e65e3d1b59/user_cropped_screenshot.png?tl_px=94,49&br_px=1470,818&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=551,277)


Tip: Paste your token in your notes. We will use this token in future steps


#### Activate your virtual environment & start your Orchestrate server


10\. Activate Virtual Environment

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/d25df99f-4b23-48cc-b68c-647f266dbff7/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=484,161)


11\. Start your Orchestrate Server

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/ff1d4c66-b35d-4194-afc0-c1d9f5820be8/user_cropped_screenshot.png?tl_px=0,0&br_px=1470,671&force_format=jpeg&q=100&width=1120.0)


12\. Paste 
```bash
orchestrate env activate local
```
 to activate your local environment

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/91f54bc5-a163-4420-b3b6-b3a2ec000cbd/user_cropped_screenshot.png?tl_px=242,0&br_px=1225,185&force_format=jpeg&q=100&width=983&wat_scale=87&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=385,126)



#### Create secure connection in Orchestrate



13\. Create the shell connection: 
```bash
orchestrate connections add -a github-demo
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/5d214cbf-bbe4-4705-b6ab-872f58cd7e35/user_cropped_screenshot.png?tl_px=192,0&br_px=1222,171&force_format=jpeg&q=100&width=1030)


14\. Configure as key/value, team-shared, bound to GitHub:

```bash
orchestrate connections configure 

-a github-demo \

--env draft \

--kind key_value \

--type team \

--url https://github.com
```
![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/7e72d114-90e4-49b6-b995-43772e71dc59/user_cropped_screenshot.png?tl_px=3,0&br_px=968,224&force_format=jpeg&q=100&width=965)


15\. Set your PAT (Paste your actual Personal Access Token): 

```bash
orchestrate connections set-credentials 

-a github-demo \

--env draft \

-e GITHUB_PERSONAL_ACCESS_TOKEN=<YOUR_PAT>
```
![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/8fc7d3f5-77b8-44ec-b5cf-51d6ea3ec748/user_cropped_screenshot.png?tl_px=0,0&br_px=1007,211&force_format=jpeg&q=100&width=1007)


16\. Verify: 
```bash
orchestrate connections list
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/86fc54ed-998f-4f93-89d6-0bb20b74f427/user_cropped_screenshot.png?tl_px=0,0&br_px=796,162&force_format=jpeg&q=100&wat_scale=71&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=363,132)


#### Import the GitHub MCP Toolkit


We will now install the official GitHub MCP Server and make its tools available to agents


17\. Paste: 
```bash
orchestrate toolkits import 

--kind mcp \

--name github-mcp \

--description "GitHub via MCP" \

--package @modelcontextprotocol/server-github \

--language node \

--tools "*" \

--app-id github-demo
```
![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/fa1843b0-ec5e-46a1-8131-a6aa15ab9ccc/user_cropped_screenshot.png?tl_px=0,0&br_px=823,259&force_format=jpeg&q=100&width=823)


18\. Verify:
```bash
orchestrate toolkits list
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/e51f8359-4e49-47ad-b7cd-bbc5b469a69c/user_cropped_screenshot.png?tl_px=0,0&br_px=1093,412&force_format=jpeg&q=100&wat_scale=97&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=843,-301)


#### Create & Import GitHub React-style agent


This agent will allow us to talk to GitHub in natural language and have the agent decide which MCP tools to call.


19\. Create a .yaml file in the directory you are currently in and paste+save:
```yaml
spec_version: v1

kind: native

name: github_helper_react

style: react

llm: watsonx/meta/llama-3-8b-instruct

description: 

GitHub helper that uses the GitHub MCP toolkit to find repositories,

summarize issues, and answer questions conversationally.

instructions: 

- When asked about repositories, use the GitHub MCP tools to search/list them.

- When asked about issues for a time window (e.g., "this week"), fetch and summarize them clearly.

- Prefer compact tabular results, then a short summary.

- Ask for confirmation before any write action.

tools: []
```
![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/bc41e90d-b384-408f-8a5d-1eeb60f5aca2/user_cropped_screenshot.png?tl_px=36,0&br_px=1183,468&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=524,768)


20\. Import the agent: 
```bash
orchestrate agents import -f agents/github_helper.yaml
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/02ac635e-0622-41e9-a456-db960eadbb8a/user_cropped_screenshot.png?tl_px=0,16&br_px=1290,838&force_format=jpeg&q=100&width=1120.0)


21\. Verify: 
```bash
orchestrate agents list
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/de2f53b8-9e5a-4f20-bd0b-778bcc09ebf9/user_cropped_screenshot.png?tl_px=0,124&br_px=1239,894&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=374,637)


#### Enable the MCP Tools for the agent (UI)


Tip: We will now Turn on the GitHub MCP Tools for the created agent


22\. Type:
```bash
orchestrate chat start
```
 in the CLI to open Orchestrate UI

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/c9f6e361-750c-402d-bc73-44c59025924b/screenshot.webp?tl_px=0,0&br_px=2190,540&force_format=jpeg&q=100&width=1120.0)


23\. You will now be brought to a UI that looks similar to the following

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/4dcf2247-eafd-49c5-aaec-1e93237e7062/screenshot.webp?tl_px=0,0&br_px=2907,1576&force_format=jpeg&q=100&width=1120.0)


24\. In the bottom left corner click "manage agents"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/b0a44fc5-a145-4cf0-9013-de83aab45732/user_cropped_screenshot.png?tl_px=0,0&br_px=2907,1576&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=20,556)


25\. Click "github_helper_react"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/c8ee1ee3-6aa1-480f-86d1-5fe7ecff5283/user_cropped_screenshot.png?tl_px=0,0&br_px=2902,1574&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=388,361)


26\. Click "Add a tool"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/6bb7ebe2-2279-4e18-82fa-706855a03839/ascreenshot.jpeg?tl_px=44,0&br_px=1420,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=524,276)


27\. Click "Add from local instance"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/3fb08b05-29e9-4831-9971-2e242e6563f9/ascreenshot.jpeg?tl_px=94,80&br_px=1470,849&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=563,277)


28\. Add tools & add to agent

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/1268768a-e6bf-4039-9413-20859d0b96d6/user_cropped_screenshot.png?tl_px=0,73&br_px=1376,842&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=114,277)


29\. Once tools have been added feel free to ask your agent "List my repositories", "Show open issues this week", or "What can you do for me?"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/a7511b40-c14b-4409-931a-24acf30a2ba0/ascreenshot.jpeg?tl_px=94,186&br_px=1470,956&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=748,511)


Tip: Congrats you are all done! In this lab, we connected Orchestrate to GitHub using the Model Context Protocol (MCP). We created a secure GitHub connection, imported the MCP toolkit, and built a React-style agent that can call GitHub tools directly and allows us to interact with GitHub in natural language.
