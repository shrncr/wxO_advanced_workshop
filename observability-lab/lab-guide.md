# Configuring Langfuse Integration
#### 


#### Creating Langfuse Project and Credentials
 

1\. Navigate to [Langfuse](https://langfuse.com/) and click this button to log in or sign up

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/eab71582-156d-4c84-911e-17b58a8b7c6f/ascreenshot.jpeg?tl_px=544,0&br_px=1920,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=955,121)


2\. Click this button to set up a new Langfuse Organization

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-22/208ee4de-6c28-4091-bfb0-14cc2f8159e7/user_cropped_screenshot.webp?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=972,109)


3\. Give your organization a name

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/d196f982-36d6-4806-8214-b1b2e5fcb002/ascreenshot.jpeg?tl_px=44,133&br_px=1367,872&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=238,316)


4\. Click "Create"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/bcee0992-d4a6-4948-b1d6-a9e4e1c56464/ascreenshot.jpeg?tl_px=0,289&br_px=1376,1058&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=261,277)


5\. Assign organization members

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-22/37144668-10c5-4541-a345-8fce2dcbc492/user_cropped_screenshot.webp?tl_px=165,151&br_px=1488,890&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=90,488)


6\. Now you will create a new project within your organization. Name it "orch-observability-lab"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/26a73624-7ab9-44ee-bdcb-9111703974b6/ascreenshot.jpeg?tl_px=20,147&br_px=1396,916&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=219,283)


7\. Click here to create an API Key for your project.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-22/17a1f2c5-4cda-4b95-b60e-d897b63be832/user_cropped_screenshot.webp?tl_px=0,50&br_px=1638,965&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=229,277)


8\. Keep This page open. We will need it for the integration.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-22/da0e7f25-7a90-4774-9c1f-d696c0363fa0/user_cropped_screenshot.webp?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=333,643)


#### Configuring Langfuse Integration with Orchestrate ADK


#### Navigate to your integrated terminal in VSCode. 

9\. Ensure your venv is activated with the following command from the `wxO_advanced_workshop` directory

```bash 
source ./.venv/bin/activate
```
 

10\. Type the following into the terminal, but **do not** yet hit enter: 
```bash 
orchestrate settings observability langfuse configure --url https://us.cloud.langfuse.com/api/public/otel --health-uri https://us.cloud.langfuse.com --project-id=
```



11\. Navigate back to the langfuse project page


12\. Press `Ctrl + C` or `Command + C` on this part of the page url to copy the project ID

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/bdb91897-0cbd-43f5-a09a-d5df2d692547/ascreenshot.jpeg?tl_px=126,0&br_px=1034,507&force_format=jpeg&q=100&width=907)


13\. Press `Ctrl + V` or `Command + V` to paste the project id back into your integrated terminal. **Do not** yet hit enter


14\. Continue typing the configuration command by typing `--api-key=`


15\. Go back to Langfuse and copy the **Secret Key**

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/59f0b682-631d-4aec-bcfc-8037a7a6a331/user_cropped_screenshot.webp?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=1025,276)


16\. Paste your Secret Key into the terminal and press `Return`. Your final command should look something like this:

```bash
orchestrate settings observability langfuse configure  --url "https://us.cloud.langfuse.com/api/public/otel"  --health-uri "https://us.cloud.langfuse.com"  --project-id "$LANGFUSE_PROJECT_ID" --api-key "$LANGFUSE_API_KEY"
```



17\. Start the Orchestrate server with Langfuse enabled by typing (the -l  argument means, "Yes, use langfuse!")
```bash 
orchestrate server start -l --env-file=./relative/path/to/env/file; 
```


18\. Activate the environment for which you'd like to set up observability. For now, let's activate our local environment with the below command:
```bash 
orchestrate env activate local
```


#### Chat With Agents
19\. Bring up your chat window by typing the following command in the terminal.
```bash 
orchestrate chat start 
```

20\. Open <http://localhost:3000/> (local environment)


21\. Chat with an agent of your choice. Langfuse will monitor all of your interactions with any agent in the activated environment.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/71d6e6ef-4ae5-4aa4-b4b4-580bf9d4b2e0/ascreenshot.jpeg?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=75,-36)


#### Observing Agent Interactions


22\. Once you are done chatting with your agent(s), navigate back to Langfuse and click "Tracing"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-22/4f45f3bc-c723-47ff-bb05-c7ec3eca28b7/user_cropped_screenshot.webp?tl_px=0,172&br_px=1323,911&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=38,189)


23\. This page will show you a table of all traces that Langfuse collected in your environment. Click on one of the traces.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/8165158d-400b-40d6-8824-24313280237f/ascreenshot.jpeg?tl_px=0,58&br_px=1376,827&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=274,277)


24\. Here you can see the preview for the selected trace.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-22/607f9ad5-a73a-4390-bb8b-aaa9d80aae55/user_cropped_screenshot.webp?tl_px=281,86&br_px=1919,1001&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=593,277)


25\. The left panel allows you to explore the depth levels of the trace, or to view all of the observations nested within your selected trace.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-22/22fd2262-f577-4b34-b320-be48f62b706a/user_cropped_screenshot.webp?tl_px=217,142&br_px=1855,1057&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=528,400)


26\. Click on an observation from the left panel.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/65a298a7-1d0c-40f1-a96a-4094b1e5be7a/ascreenshot.jpeg?tl_px=272,206&br_px=1910,1122&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=885,449)


27\. Click here to download the trace data

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/d13173e4-238b-4e2f-bf3f-96d0b975d0d0/user_cropped_screenshot.webp?tl_px=514,157&br_px=1624,777&force_format=jpeg&q=100&width=1110&wat_scale=99&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=433,50)


28\. Click here to structure observations as a timeline

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/a41f8326-7bc0-4620-a07f-25add1974168/user_cropped_screenshot.webp?tl_px=497,143&br_px=1607,763&force_format=jpeg&q=100&width=1110&wat_scale=99&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=512,66)


29\. Click here to change the trace view settings

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/879abe6a-1936-4a16-bf6f-6c7180bc8000/ascreenshot.jpeg?tl_px=415,149&br_px=1525,769&force_format=jpeg&q=100&width=1110&wat_scale=99&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=491,60)


30\. Click here to view a table of observations

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/e44be3c6-e2a3-448d-912b-a39b875aba0c/ascreenshot.jpeg?tl_px=233,154&br_px=1343,774&force_format=jpeg&q=100&width=1110&wat_scale=99&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=114,94)


31\. Click an observation

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/44acbdd6-6d8c-4f56-8527-9209765c3974/ascreenshot.jpeg?tl_px=204,171&br_px=1187,721&force_format=jpeg&q=100&width=983&wat_scale=87&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=352,234)


# Recap & Next Steps

In this lab, you connected Orchestrate to Langfuse and saw firsthand how observability can give you a clear window into agent behavior. You configured integrations, chatted with agents, and explored how traces and observations reveal exactly what’s happening inside each interaction.

By showing customers what’s happening under the hood of an AI agent, you can:

- Highlight transparency and trust by walking them through traces.

- Show how issues can be diagnosed quickly, reducing risk.

- Position observability as a way to measure and prove value, not just to monitor.

- Create more compelling stories when presenting solutions — because you can back them up with data.

The more you can show customers the why behind a system’s behavior, the more powerful your demos and PoCs become, and the more you can prove IBM is *trusted* for enterprise AI

## Optional Challenge!

Now that you’ve seen observability in action, try this experiment:

Chat with a React-style Agent – This agent makes its reasoning visible step by step. Notice how the traces align with the reasoning chain, making it easy to explain decisions.

Chat with a non-React Agent – This one gives results directly, with less visibility into its process. Look at the traces and compare what you can and can’t see.

👉 Reflect: Which experience feels more trustworthy and demo-friendly? How might you use these differences in a customer conversation?
