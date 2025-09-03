import smtplib
from email.mime.text import MIMEText
from pydantic import BaseModel, Field
import json
from ibm_watsonx_orchestrate.run import connections
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission
'''

    DO NOT CHANGE THIS FILE

'''
@tool(
    permission=ToolPermission.READ_ONLY,
    name="send_email_gmail",
    description="sends an email"
)
def send_gmail_email(to_email: str, subject: str, body: str) -> str:
    """
    Sends email

    Returns:
        str: A dict object
    """
    
    # make an app password for your email at https://myaccount.google.com/apppasswords 
    conn = connections.basic_auth("gmail")
    gmail_user = conn.username
    app_password = conn.password

    #mime msg
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = to_email

    #try catch block to send email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(gmail_user, app_password)
            smtp.send_message(msg)
        return f"Email with body \"{body}\" and subject: \"{subject}\" \n sent successfully to {to_email}!"
    except Exception as e:
        return (f"Error sending email: {e}")