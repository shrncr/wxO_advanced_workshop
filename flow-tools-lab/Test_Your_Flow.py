import asyncio
import logging
from pathlib import Path
from tools.flow import build_f1_flow
from ibm_watsonx_orchestrate.flow_builder.flows.flow import FlowRunStatus
from ibm_watsonx_orchestrate.flow_builder.types import FlowEventType
'''
This file allows you to test any flow
In future flow developmemt, you can simply reuse this Test_Your_Flow python file to test any flow tools you create.
Right now, we are using the file to test our F1 Flow tool.

Line 4 imports the flow tool you plan to test (right now, it's build_f1_flow)
Line 40 contains the input data that is given to the flow's start node. Right now, you will simply change the email address provided to the input

'''
logger = logging.getLogger(__name__)

flow_run = None

def on_flow_end(result):
    """
    Callback function to be called when the flow is completed.
    """
    print(f"Custom Handler: flow `{flow_run.name}` completed with result: {result}")

def on_flow_error(error):
    """
    Callback function to be called when the flow fails.
    """
    print(f"Custom Handler: flow `{flow_run.name}` failed: {error}")


async def main():
    '''A function demonstrating how to build a flow and save it to a file.'''
    my_flow_definition =  await build_f1_flow().compile_deploy()

    current_folder = f"{Path(__file__).resolve().parent}"
    
    global flow_run
    flow_run = await my_flow_definition.invoke(input_data={"input": "please send a f1 update to <Email-here>"},
                                               on_flow_end_handler=on_flow_end, 
                                               on_flow_error_handler=on_flow_error, 
                                               debug=True)
    

if __name__ == "__main__":
    asyncio.run(main())
