#test_tool.py
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission

@tool(name="make_uppercase", description="Returns context variables to the agent", permission=ToolPermission.ADMIN)
def my_tool(input: str) -> str:
    """Returns a variable called merged_data.

    Converts the input string to uppercase and returns it as merged_data.

    Args:
        input (str): The input of the tool.

    Returns:
        A string containing the modified string.
        
        str: merged_data 
        For example:
        merged_data=DBENNER@IBM.COM
    """

    #functionality of the tool
    merged_data = input.upper()
    
    # This line sets the context variable merged_data in the agent.
    return f"merged_data={merged_data}" 
    