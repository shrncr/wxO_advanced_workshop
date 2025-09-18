# Building Flow Tools in Orchestrate

This lab guide will walk you through creating a flow tool in the ADK. The tool will:
1. Perform a web search for the most recent Formula 1 event  
2. Use a generative node to write an exciting email update  
3. Send the email to a chosen recipient  

> ⚠️ **Important Alert: Python Indentation**
>
> In this lab guide, you will see both **screenshots** and **code snippets**.  
> Python relies heavily on **whitespace and indentation**. If indentation is off, your code will throw errors (such as `IndentationError` or unexpected behavior).
>
> ✅ **Always copy code from the code snippets, not from screenshots.**  
> After pasting, double-check that the indentation matches exactly.
>
> If you see errors related to indentation, carefully re-align the code before running it.


### Exploring the Files


1\. Open the flow-tools-lab folder

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/c9719f2b-4567-4467-aa35-8769bead2adc/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=44,102)


2\. Open the tools folder

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/add72bc5-4589-4da0-88f5-d87a325c7206/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=51,161)


3\. Look at `web_search.py` and `gmail.py`. The source code for these tools should already be completed. **Do not change these files**.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/ace19b2a-9337-4ea7-b257-5b9d7faac959/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=115,249)


4\. Click here. Look at `requirements.txt`. The source code for this file should already be completed. **Do not change this file**.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/42350e07-3a02-4294-96a4-794015a0c27c/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=121,213)


5\. Click here to open `flow.py`. This is where we will build our tool flow.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/badba0b7-8b59-4039-aa3e-9b1ba5904291/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=349,156)


### Creating the Flow Tool


6\. Replace the current contents of the file with these import statements.

Lines 1-3 import libraries that will help our flow understand the data types that flow through our tool's nodes.

Line 4 imports the different node types we plan to use in this lab 

Lines 5 and 6 import the web_search and send_gmail_email tools that we looked at in previous steps. We will include both of these tools as nodes in our flow.

```python
from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel, Field
from ibm_watsonx_orchestrate.flow_builder.flows import END, Flow, flow, START, PromptNode, AgentNode, UserNode
from .web_search import web_search
from .gmail import send_gmail_email
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/a63cf2ba-83de-4ef7-b666-f58b8e6c63ab/ascreenshot.jpeg?tl_px=0,0&br_px=1938,1083&force_format=jpeg&q=100&width=1120.0)


7\. Create the f1_prompt_result_data Pydantic class. This class represents be the output structure of our generative AI node

```python
class f1_prompt_result_data(BaseModel):
    body: str = Field(description="Body content of Formula 1 Race email update")
    Subject: str = Field(description="Subject line for Formula 1 Race email update")
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/c51f8113-9942-40b2-9622-303ad823ad52/ascreenshot.jpeg?tl_px=258,36&br_px=1308,623&force_format=jpeg&q=100&width=1050)


8\. Now create the class F1_Race_Data. This will be the output schema for our web_search tool node

```python
class F1_Race_data(BaseModel):
    race_data: str = Field(description="race data for most recent Formula 1 Race")
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/70f5d0de-ec5c-4370-9b18-f8eb53a7b678/ascreenshot.jpeg?tl_px=298,56&br_px=1209,566&force_format=jpeg&q=100&width=911)


9\. Now, create the class for Final_Email_Data. This schema represents the input required for our send_gmail_email tool node

```python
class Final_Email_Data(BaseModel):
    to_email: str = Field(description="Who to send the email to")
    subject: str = Field(description="Subject line for Formula 1 Race email update")
    body: str = Field(description="Body content of Formula 1 Race email update")
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/56fa1700-47ff-4af9-8007-35d10d080498/ascreenshot.jpeg?tl_px=235,0&br_px=1285,587&force_format=jpeg&q=100&width=1050)


10\. Now, we will begin to develop our generative_prompt node. This function will take in a flow object as an input, and return a 'PromptNode' as an output
```python
def generative_prompt(aflow: Flow) -> PromptNode:
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/6c82d19d-f506-48bb-b0c8-3c0a1e9c4517/ascreenshot.jpeg?tl_px=243,487&br_px=1294,1074&force_format=jpeg&q=100&width=1050)


11\. Now we make a variable 'prompt_node' which is of type 'prompt'

```python
    prompt_node = aflow.prompt(
```
![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/b6920462-a6aa-413c-8a15-c4130db529d7/ascreenshot.jpeg?tl_px=148,368&br_px=1198,955&force_format=jpeg&q=100&width=1050)


12\. Now we input the information that is required to run our prompt node successfully, starting with our prompt node's name
```python
        name="generate_f1_update",
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/e8b7cf6f-fe8d-4660-9a2e-28fa41e474dd/ascreenshot.jpeg?tl_px=0,74&br_px=1938,1158&force_format=jpeg&q=100&width=1120.0)


13\. next, we create the prompt node's display name. this is what will appear if you view the flow from the orchestrate flow builder UI

```python
        display_name="Generate a report on the most recent Formula 1 race",
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/ed564234-d141-4ff0-8c38-de83bc3e82e0/ascreenshot.jpeg?tl_px=0,74&br_px=1938,1158&force_format=jpeg&q=100&width=1120.0)


14\. Now, we add a description to our generative prompt tool

```python
        description="Generate a report on the most recent Formula 1 race",
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/9d962962-b86c-4a8e-8565-3dfd055f45c5/ascreenshot.jpeg?tl_px=0,74&br_px=1938,1158&force_format=jpeg&q=100&width=1120.0)


15\. Now add the system prompt, this is a description informing the node of it's general purpose and how it the LLM should behave

```python
        system_prompt=[
            "You are an assistant who generates Formula 1 Race updates"
        ],
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/f0f4186f-6c20-4c66-8056-54fb7eae6f6e/ascreenshot.jpeg?tl_px=0,74&br_px=1938,1158&force_format=jpeg&q=100&width=1120.0)


16\. Now we add the user prompt, which is what you yourself would say to the generative node to yield some response

```python
        user_prompt=[
            "Turn this data into an exciting Formula 1 Race update to a formula 1 fan. Here is the data: "
        ],
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/f2d641e1-83c9-4a95-9761-d0ced2d41935/ascreenshot.jpeg?tl_px=0,74&br_px=1938,1158&force_format=jpeg&q=100&width=1120.0)


17\. Now we choose the llm. I chose watsonx/meta-llama/llama-4-maverick-17b-128e-instruct-fp8 .

```python
        llm="watsonx/meta-llama/llama-4-maverick-17b-128e-instruct-fp8",
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/a3d8c0a5-5bae-4b5b-b7ae-8a4ac9d5f7da/ascreenshot.jpeg?tl_px=243,500&br_px=1294,1087&force_format=jpeg&q=100&width=1050)


18\. Now input llm parameters. You can keep these the same as mine, or you may adjust them to your liking

```python
        llm_parameters={    
            "temperature": .4,
            "min_new_tokens": 50,
            "max_new_tokens": 200,
            "top_k": 30,
            "stop_sequences": ["Human:", "AI:"]
        },
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/19542632-bb3f-4039-8760-25f1adabbd2d/ascreenshot.jpeg?tl_px=188,433&br_px=1099,943&force_format=jpeg&q=100&width=911)


19\. tell the node what input format it should expect with `input_schema=F1_Race_data`

```python
        input_schema=F1_Race_data,
```


![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/876b2ff9-3c87-434d-8d90-404089e7c83a/ascreenshot.jpeg?tl_px=258,488&br_px=1169,997&force_format=jpeg&q=100&width=911)


20\. Tell the node what its output should look like with `output_schema=f1_prompt_result_data` (Yes, include the closing parentheses)

```python
        output_schema= f1_prompt_result_data
    )
```
![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/636f7b45-2d28-4451-9cea-dd7f93234124/ascreenshot.jpeg?tl_px=288,571&br_px=1052,999&force_format=jpeg&q=100&width=764&wat_scale=68&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=522,184)


21\. Now have your generative_prompt function return the prompt_node variable by typing `return prompt_node`

```python
    return prompt_node
```
![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/2aeeeec6-9ee0-4830-8df3-713d99b559bb/ascreenshot.jpeg?tl_px=213,430&br_px=1195,979&force_format=jpeg&q=100&width=983&wat_scale=87&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=348,365)


22\. Now its time to build our flow. Use `@flow` to indicate the start of your flow tool definition. Give your flow a name, define your flow's input schema, and define its output schema. We expect our input and output to simply be strings

```python
@flow(
        name = "f1_update_flow",
        input_schema=str,
        output_schema=str,
        schedulable=True
    )
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/468fe9cc-f024-4896-bb36-ecf1b5990e20/ascreenshot.jpeg?tl_px=165,589&br_px=969,1038&force_format=jpeg&q=100&width=805)


23\. You will start your flow  with a function definition

```python
def build_f1_flow(aflow: Flow = None) -> Flow:
```
![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/403387fc-a4f3-4bc0-ae06-0f0d5e28b71b/ascreenshot.jpeg?tl_px=208,650&br_px=1013,1100&force_format=jpeg&q=100&width=805)


24\. Create a header explaining what this flow is for

```python
    """
    Build a simple system that will generate status reports on the most recent F1 Race    
    """
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/cd9cc297-bff5-4b1d-b4ca-8dfa07cf37c7/ascreenshot.jpeg?tl_px=0,388&br_px=1376,1158&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=320,338)


25\. Create your web_search_tool_node, which will search the web for Formula 1 data

```python
    web_search_tool_node= aflow.tool(web_search)
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/9517092f-2047-48c0-a9c1-23f64ebcdeda/ascreenshot.jpeg?tl_px=229,388&br_px=1606,1158&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=524,378)


26\. Now define your email_generator node, which will use the llama maverick model to generate a creative email subject and body to be sent out

```python
    update_email_generator_node = generative_prompt(aflow)
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/1624127d-b041-4892-8b11-f64522007e1a/ascreenshot.jpeg?tl_px=282,660&br_px=1003,1063&force_format=jpeg&q=100&width=720)


27\. Now define your send_gmail_update node, which will use the send_gmail_email tool to send out the generated email

```python
    send_gmail_update_node = aflow.tool(send_gmail_email, input_schema=Final_Email_Data)
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/5d0f3000-02f6-4ea8-a56c-35fee0d439ca/ascreenshot.jpeg?tl_px=256,510&br_px=1307,1097&force_format=jpeg&q=100&width=1050)


28\. Use the **aflow.sequence** function to define the order in which these nodes should be completed. Here, you see we begin with out start node, then move to our generative node, then move to our send_email node, and finally transition to our end node, which completes the flow

```python

    aflow.sequence(START, web_search_tool_node, update_email_generator_node, send_gmail_update_node, END)
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/f8eb46b1-9ee7-4fe6-9a33-aa05a0c42cb3/ascreenshot.jpeg?tl_px=339,509&br_px=1389,1096&force_format=jpeg&q=100&width=1050)


29\. Lastly, return the flow by typing `return aflow`

```python
    return aflow
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/fddfe278-a138-45b3-a22f-5138a2480890/ascreenshot.jpeg?tl_px=0,74&br_px=1938,1158&force_format=jpeg&q=100&width=1120.0)


### Getting Credentials for Gmail
>If you don't have a gmail account already, you can follow my lab guide on creating a gmail account here:  [creating-new-gmail.md](./creating-new-gmail.md "Gmail account how to")

30\. Navigate back to gmail.py and Press `Ctrl + C` on the link provided in line 25

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/9aa7327c-bc6e-46ee-8dd9-0ea61fb91bb8/ascreenshot.jpeg?tl_px=0,74&br_px=1938,1158&force_format=jpeg&q=100&width=1120.0)


31\. Paste the link in a browser of your choice. You will be prompted to sign in.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/addec8ef-de70-4662-b3dc-738b3d8d838f/user_cropped_screenshot.webp?tl_px=0,0&br_px=1428,1043&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=630,329)


32\. Click this text field.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/ebee77d4-8eb5-421f-ac29-d39d8b0ec0bd/user_cropped_screenshot.webp?tl_px=0,0&br_px=1428,1043&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=310,589)


33\. Name your app "Orchestrate-App-Password, " or another name of your choosing


34\. Click "Create"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/1d0a2862-6fbd-494f-8332-405e3ab7ccd7/user_cropped_screenshot.webp?tl_px=0,0&br_px=1428,1043&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=644,689)


35\. You will be given a 16-Character long app password. Press `ctrl + c` or `command + c` to copy this and store it in a safe space

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/88e42729-e58c-403a-8fdc-a7e98cb24154/user_cropped_screenshot.webp?tl_px=0,0&br_px=1428,1043&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=634,298)


### Importing Your Gmail Tool
#### The following instructions will take place in either Ubuntu or ZSh terminal. Step 40 assumes you are working from the flow-tools-lab directory


36\. 
```bash 
orchestrate env activate <environment-name>
````


37\. 
```bash 
orchestrate connections add --app-id gmail
```


38\. 
```bash 
orchestrate connections configure --app-id gmail --env draft --type member --kind basic
```


39\. 
```bash
orchestrate connections set-credentials --app-id gmail --env draft -u <youremail> -p <your app password, should look like xxxx xxxx xxxx xxxx>
```


40\. 

```bash
orchestrate tools import -k python -f ./tools/gmail.py --app-id gmail
```


### Importing Your Web_Search Tool


> **Alert: We configured Tavily credentials and a web search tool in previous labs. You DO NOT need to re-configure Tavily if you have done so already. IF YOU HAVE COMPLETED THE TOOLS LAB, you only need to follow the instructions for the gmail credentials and tool**

#### The following instructions will take place in either Ubuntu or ZSh terminal. Step 44 assumes you are working from the flow-tools-lab directory

41\. 
```bash
orchestrate connections add --app-id tavily 
```


42\. 
```bash
orchestrate connections configure --app-id tavily --env draft --type member --kind api_key
```


43\. 
```bash
orchestrate orchestrate connections set-credentials --app-id tavily --env draft -k <put-key-here>
```


44\. 
```bash
orchestrate tools import -k python -f ./tools/web_search.py --app-id tavily
```


### Testing your Flow


45\. activate your local environment with 
```bash
orchestrate env activate <env-name>
```


46\. Navigate to Test_Your_Flow.py

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/49ea45c9-bf5a-4d8e-9a6a-fd6e2b86fc60/ascreenshot.jpeg?tl_px=0,1&br_px=1376,770&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=100,277)


47\. Go to the line which defines "input" and replace <email-here> with the email you'd like to send the update to

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/9d8c9cb2-cc06-47a2-abcd-38b784d1f0e3/ascreenshot.jpeg?tl_px=561,59&br_px=1938,828&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=611,276)


48\. Press `Ctrl + S` or `Command + S` to save your changes

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/26b48c7c-be9a-4f13-a415-c0b4cbcf980b/ascreenshot.jpeg?tl_px=0,0&br_px=1938,1083&force_format=jpeg&q=100&width=1120.0)


49\. Click the **Run and Debug** icon on the left panel of vscode

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/4c9c89d2-07a1-4213-8499-0263453ee6e6/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=-1,163)


50\. Click the **run and debug** button

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/88be1df5-51f7-44fd-89b6-78e9e679d22e/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=111,103)


51\. Choose **python debugger**

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/88b0db30-1e36-4746-8d80-0a0bf9b11ec6/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=494,17)


52\. Make your terminal large enough so you can view the logs. You may receive an error at the end, but the email will still go through

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/cd0981ee-b3a4-4f94-946e-11c6f503ca49/ascreenshot.jpeg?tl_px=186,388&br_px=1562,1158&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=524,483)


53\. view the debugger logs

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/7a5889d4-9533-40d7-8ef0-86c70ad91b74/ascreenshot.jpeg?tl_px=65,370&br_px=1442,1139&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=524,277)


### Adding the Flow to an Agent


54\. Click the explorer icon to navigate back to your project folder

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/db055fa8-8d18-4161-9a12-9174f83ba4f6/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=0,27)


55\. Click into the agent folder

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/d7a4a769-f539-49e2-ae18-6be409b7605e/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=86,121)


56\. Click on agent.yaml

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/61e86bba-13ba-440b-b6a3-1ce3d171db70/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=95,141)


57\. Add your flow tool to the agent spec

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/ce9fbaf6-de3a-4f82-930d-a98015f4d5fb/ascreenshot.jpeg?tl_px=87,0&br_px=1464,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=524,266)


58\. Press `Ctrl + S` to save your file

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/27249c14-2fc5-40ed-83e4-37eb22f08e64/ascreenshot.jpeg?tl_px=0,0&br_px=1938,1083&force_format=jpeg&q=100&width=1120.0)


### Importing Via the ADK


59\. 
```bash 
orchestrate tools import -k flow -f ./tools/flow.py
```


60\. Assuming you are working from the flow-tools-lab directory
```bash 
orchestrate agents import -f ./agents/agent.yaml
```


### Using Your Flow


61\. Click the "Filter agent" field.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/7a4294e5-c953-4b01-9efd-0ff2d1a00855/ascreenshot.jpeg?tl_px=0,0&br_px=1427,797&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=249,111)


62\. Click "F1_Updater_Agent"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/ae513372-afbd-43b6-a670-e888a7ad7488/ascreenshot.jpeg?tl_px=0,0&br_px=1427,797&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=131,178)


63\. Click the "Type something..." field.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/579a5b56-3b06-4cf4-a6e3-202347fd8ab0/ascreenshot.jpeg?tl_px=0,245&br_px=1427,1043&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=398,540)


64\. Type "email [&lt;email-here&gt;](mailto:loveyawink@gmail.com) with updates for the most recent formula 1 race" and hit `Enter`


65\. And then the workflow will kick off and send out an F1 Update!

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/5bb71121-aff7-42a3-aa6a-d3ea73b9ef57/user_cropped_screenshot.webp?tl_px=321,156&br_px=1350,731&force_format=jpeg&q=100&width=1030&wat_scale=91&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=445,381)

# Recap & Next Steps

In this lab, you built a flow tool in Orchestrate using the ADK. You combined multiple nodes — a web search, a generative prompt, and a Gmail integration — into a working system that automatically emails a Formula 1 race update. Along the way, you:

- Explored how different node types (tool, prompt, flow) can be chained together.

- Used schemas to clearly define inputs and outputs for each step.

- Learned how to import tools, configure connections, and attach your flow to an agent.

This type of orchestration is powerful for customer-facing scenarios. Instead of just showing an agent responding in chat, you can demo end-to-end automation: pulling data, generating value-added content, and delivering it through a real channel (like email). It shows customers how Orchestrate can be both flexible and production-ready, with flows that map directly to real business processes.

## Challenge

Now it’s your turn to extend the flow. Try one of the following:

- Scheduling: Check the ADK documentation
 and make your flow schedulable. For example, set it to run automatically at the end of the next Formula 1 race.

- Human-in-the-loop: Add a UserNode so a human can approve or edit the email before it’s sent.

- Customize: Add a new node of your choice — maybe a summary step, a translation step, or a Slack notification.

👉 The goal is to experiment with how flows can be adapted to different customer scenarios. Think about how each adjustment could strengthen your demos or open new conversations in a sales cycle.
