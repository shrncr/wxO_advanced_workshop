# Orchestrate Tool Lab

In this lab, you'll build a Python-based web search tool using the Tavily API and Orchestrate ADK. You'll:

1. Write the python code for the tool

2. Use the Orchestrate Connections Vault to securely access your API key

3. Add your tool to an agent spec

4. Import your tool and agent into an Orchestrate environment of your choice

Note: You must complete the previous lab (where you set up your Tavily API connection) before starting this one.

> ⚠️ **Important Alert: Python Indentation**
>
> In this lab guide, you will see both **screenshots** and **code snippets**.  
> Python relies heavily on **whitespace and indentation**. If indentation is off, your code will throw errors (such as `IndentationError` or unexpected behavior).
>
> ✅ **Always copy code from the code snippets, not from screenshots.**  
> After pasting, double-check that the indentation matches exactly.
>
> If you see errors related to indentation, carefully re-align the code before running it.


## Section 1 : Creating the Connection to Tavily
1\. 
```bash
orchestrate connections add --app-id tavily 
```


2\. 
```bash
orchestrate connections configure --app-id tavily --env draft --type member --kind api_key
```


3\. 
```bash
orchestrate orchestrate connections set-credentials --app-id tavily --env draft -k <put-key-here>
```


## Section 2: Creating the Tavily Web Search Tool
1\. Navigate to the tools-lab folder, open the tools folder, and then open web_search.py

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/2c6a96ad-4b62-48aa-864e-5f3b5dddf6f5/ascreenshot.jpeg?tl_px=0,77&br_px=982,626&force_format=jpeg&q=100&width=983&wat_scale=87&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=151,267)


2\. Add these three lines to the top of your `web_search.py` file:

```python
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission #This lets you use the `@tool` decorator to turn your function into a usable tool.
from ibm_watsonx_orchestrate.run import connections #This gives you access to the Tavily credentials you set up in the previous lab.
from tavily import TavilyClient #This imports the Tavily Python module so you can interact with the Tavily API.
```


![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/d43daf66-02f4-4dc7-a88b-f731d42c815e/ascreenshot.jpeg?tl_px=248,0&br_px=1159,509&force_format=jpeg&q=100&width=911)


3\. Use the `@tool` decorator to start setting up your tool. This decorator lets you give your tool a **name**, a **description**, and set **permissions**. This helps others (and the system) understand what your tool does and when it can be used.

```python
@tool(name="web_search", description="Search the web.", permission=ToolPermission.READ_ONLY)
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/28120000-7aaf-4eda-b000-a421e402ad0f/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=283,177)


4\. This line defines the function that your tool will run.\
It takes one input:

- `query`: a string that represents the user’s search question.

The function returns a `dict` (dictionary), which will contain the response from the Tavily Search API.

```python
def web_search(query: str) -> dict:
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/acd63230-603c-4815-8f43-df5af8b18de3/user_cropped_screenshot.webp?tl_px=183,47&br_px=1123,573&force_format=jpeg&q=100&width=940&wat_scale=83&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=230,203)


5\. Add a header to the top of your function. This will describe the tool, and explain the inputs and outputs of the function. You may use mine, or create your own.

```python
    """
    Search the web for relevant information using Tavily Search.

    Args:
        query (str): The search query string.
        url (str): the url where search results must come from

    Returns:
        dict: A dictionary of search results obtained from Tavily search.
    """
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/7eaff3d3-367d-404e-9eaa-be8d7bab12fe/user_cropped_screenshot.webp?tl_px=341,129&br_px=1201,609&force_format=jpeg&q=100&width=860&wat_scale=76&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=702,222)


6\. Add a try-except block as shown below. Your tool will try to call out to the Tavily API, and if it cannot, the except block will handle the error.


```python
    try:
        
    except Exception as e:
       
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/1dbd35dc-c4f0-47ee-9d2a-96d6cb9b4e79/user_cropped_screenshot.webp?tl_px=229,188&br_px=994,615&force_format=jpeg&q=100&width=764&wat_scale=68&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=466,247)


7\. Add this line to create a variable called `conn`, which will store the authentication details for the `"tavily"` connection. This connection was defined earlier in the previous lab. The `api_key_auth` method retrieves the API key you saved and makes it accessible through the `conn` object without revealing it in your tool's code.

```python
        conn = connections.api_key_auth('tavily')
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/58255887-3303-4ed8-a7f9-1f7fdd03668c/ascreenshot.jpeg?tl_px=259,260&br_px=1063,710&force_format=jpeg&q=100&width=805)


8\. In this line, you create an object named `tavily_client`, which initializes a connection to the Tavily API using the `TavilyClient` class from the `tavily` module (imported in step 2). You're passing `conn.api_key` as the value for the `api_key` parameter—this provides the client with the credentials it needs to authenticate with the API.

```python
        tavily_client = TavilyClient(api_key=conn.api_key)
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/1e2e1366-2aa6-4664-ac01-d50e567ccf51/ascreenshot.jpeg?tl_px=396,234&br_px=944,540&force_format=jpeg&q=100&width=548)


9\. This line uses the `tavily_client` to send a search request to the Tavily API.

- It searches using the user's question (`query`)

- It asks for up to 5 results

- It also asks the API to include a short answer (`include_answer=True`)

  \
  The result is saved in a variable called `response`.
  
if a response is successfully generated, then it is returned to the agent.

```python
        response = tavily_client.search(query=query, max_results=5, include_answer=True)
        
        return response
```
![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/47334249-55ea-49f3-b2be-bb7e9ebdb53c/ascreenshot.jpeg?tl_px=0,0&br_px=1938,1083&force_format=jpeg&q=100&width=1120.0)


10\. Add this line inside your `except` block. It will print out the error message if something goes wrong, which helps you understand what the problem is.

```python
       return (f"Unexpected Error: {e}")
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/600605d0-b5bd-416a-925a-619151d8bf41/ascreenshot.jpeg?tl_px=267,38&br_px=1644,807&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=524,277)


11\. Press `Ctrl + S`to save your code



12\. Open the requirements file in your tool folder.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/4af6c956-cc8b-42c5-ab9b-43b1ab7c4a9e/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=120,257)


13\. Since we used a non-native Python module in our code, we need to add its name (`tavily-python`) to the `requirements.txt` file. This file lists all the external packages your code needs to run.

Adding the module here makes sure that when the tool is installed or deployed, it automatically installs everything it needs so your tool runs smoothly.

Remember to press `Ctrl + S` to save your file.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/ca0b12a7-3c36-4570-a948-aa0f9a700c82/ascreenshot.jpeg?tl_px=37,34&br_px=1087,621&force_format=jpeg&q=100&width=1050)


14\. This lab includes an agent specification so you can test your tool. Navigate to tools-lab/agents/agent.yaml, and add the web_search tool to your agent specification.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/0c365aa7-1ec8-4866-8e9a-8b8457b12ddc/ascreenshot.jpeg?tl_px=0,0&br_px=1938,1083&force_format=jpeg&q=100&width=1120.0)


15\. In your terminal and from the `tools-lab` directory, type the command below to import your web_search tool

```bash
orchestrate tools import -f ./tools/web_search_tool/web_search.py -r ./tools/web_search_tool/requirements.txt -k python --app-id tavily
```
15\. Ensure your virtual environment is activated, orchestrate server is running, and that you are connected to your local environment. 


16\. In your terminal and from the `tools-lab` directory, type the command below to import your web_search tool. This is where you upload your web-researcher agent to Orchestrate!

```bash 
orchestrate agents import -f ./agents/agent.yaml
```


17\. Go to a web browser, log into your Orchestrate environment, and chat with your web_researcher agent!

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/cb01723b-79f2-4b5f-9b8e-1169d7930f75/screenshot.webp?tl_px=0,0&br_px=1218,820&force_format=jpeg&q=100&width=1120.0)

# Recap & Next Steps

In this lab, you created a Python-based web search tool with the Tavily API and integrated it into Orchestrate. Along the way, you worked with:


- The Tavily client to query search results programmatically

- Agent specs and tool specs to connect your tool into an Orchestrate environment

You now have a repeatable pattern for adding external APIs into agents and showcasing them in live environments. When building demos or proof-of-concepts, this skill helps you:

- Show customers how Orchestrate can quickly extend to third-party services

- Use real search results to ground agent responses in fresh data

- Create flexible demos where you can adapt the tool to different industries, use cases, or data needs


## Challenge

To take this further, explore the Tavily API Playground:

1. Go to the Tavily API Playground
.

1. Use the UI to change the filters — for example, adjust sources, date ranges, or result types.

3. Notice how the Playground automatically generates a code snippet for your custom query!

👉 Try copying one of these snippets back into your web_search.py function and rerun your tool.

> Reflect:
>
>How does changing filters change the quality and type of data you get back?
>
>How could you use this to adapt a demo for different customer scenarios?
