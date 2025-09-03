from datetime import datetime
from typing import Any, Optional
from pydantic import BaseModel, Field
from ibm_watsonx_orchestrate.flow_builder.flows import END, Flow, flow, START, PromptNode, AgentNode, UserNode
from .web_search import web_search
from .gmail import send_gmail_email


#pydantic classes to define input/output schemas for nodes
class f1_prompt_result_data(BaseModel):
    body: str = Field(description="Body content of Formula 1 Race email update")
    Subject: str = Field(description="Subject line for Formula 1 Race email update")
class F1_Race_data(BaseModel):
    race_data: str = Field(description="race data for most recent Formula 1 Race")
class Final_Email_Data(BaseModel):
    to_email: str = Field(description="Who to send the email to")
    subject: str = Field(description="Subject line for Formula 1 Race email update")
    body: str = Field(description="Body content of Formula 1 Race email update")
    

#node which generates the f1 update email body and subject
#you may adjust arguments to your liking
def generative_prompt(aflow: Flow) -> PromptNode:
    prompt_node = aflow.prompt(
        name="generate_f1_update",
        display_name="Generate a report on the most recent Formula 1 race",
        description="Generate a report on the most recent Formula 1 race",
        system_prompt=[
            "You are an assistant who generates Formula 1 Race updates"
        ],
        user_prompt=[
            "Turn this data into an exciting Formula 1 Race update to a formula 1 fan. Here is the data: "
        ],
        llm="watsonx/meta-llama/llama-4-maverick-17b-128e-instruct-fp8",
        llm_parameters={    
            "temperature": .4,
            "min_new_tokens": 50,
            "max_new_tokens": 200,
            "top_k": 30,
            "stop_sequences": ["Human:", "AI:"]
        },
        
        input_schema=F1_Race_data,
        output_schema= f1_prompt_result_data
    )
    return prompt_node

@flow(
        name = "f1_update_flow",
        input_schema=str,
        output_schema=str,
        schedulable=True
    )
def build_f1_flow(aflow: Flow = None) -> Flow:
    """
    Build a simple system that will generate status reports on the most recent F1 Race    
    """
    web_search_tool_node= aflow.tool(web_search)
    update_email_generator_node = generative_prompt(aflow)
    send_gmail_update_node = aflow.tool(send_gmail_email, input_schema=Final_Email_Data)

    aflow.sequence(START, web_search_tool_node, update_email_generator_node, send_gmail_update_node, END)

    return aflow