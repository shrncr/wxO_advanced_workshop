# Configuring Langfuse Integration
#### [Made by Sara Hrnciar with Scribe](https://scribehow.com/shared/Configuring_Langfuse_Integration__aRsQFGhcQQGvKJsHxe8h5g)


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


9\. Open a new terminal

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-22/bde4d056-5aae-4dde-8a43-610e01a2e5ac/user_cropped_screenshot.webp?tl_px=0,0&br_px=1638,915&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=441,235)


10\. Type the following into the terminal: 
```bash 
orchestrate settings observability langfuse configure --url https://us.cloud.langfuse.com/api/public/otel --health-uri https://us.cloud.langfuse.com --project-id
```
![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/7741245a-7eda-4f81-abe2-955a30dccd45/ascreenshot.jpeg?tl_px=141,0&br_px=1860,961&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=524,193)


11\. Navigate back to the langfuse project page

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-22/f9cd0943-d8d3-4228-9018-324ed6ba696c/user_cropped_screenshot.webp?tl_px=49,0&br_px=1373,739&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=358,26)


12\. Press `Ctrl + C` on this part of the page url to copy the project ID

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/bdb91897-0cbd-43f5-a09a-d5df2d692547/ascreenshot.jpeg?tl_px=126,0&br_px=1034,507&force_format=jpeg&q=100&width=907)


13\. Press `Ctrl + V` to paste the project id

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/7c09e3a5-f454-421a-9615-b13dc3375dbd/ascreenshot.jpeg?tl_px=0,126&br_px=1919,1200&force_format=jpeg&q=100&width=1120.0)


14\. Continue typing the configuration command by typing `--api-key`

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/42a2c378-3723-4079-8d3f-2326eb661c48/ascreenshot.jpeg?tl_px=544,0&br_px=1920,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=955,160)


15\. Go back to Langfuse and copy the **Secret Key**

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/59f0b682-631d-4aec-bcfc-8037a7a6a331/user_cropped_screenshot.webp?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=1025,276)


16\. Paste your Secret Key into the terminal and press `Return`

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-22/e6dba3a7-1ede-46ef-bb0e-90f1081b5fe2/user_cropped_screenshot.webp?tl_px=84,0&br_px=1722,915&force_format=jpeg&q=100&width=1120.0)


17\. Start the Orchestrate server by typing 
```bash 
orchestrate server start -l --env-file=<./relative/path/to/env/file>; 
```


18\. Activate the environment for which you'd like to set up observability.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/bd2b0959-6415-4a9f-972d-23547c1f17a5/user_cropped_screenshot.webp?tl_px=140,142&br_px=1779,1057&force_format=jpeg&q=100&width=1120.0)


#### Chat With Agents


19\. Open <https://dl.watson-orchestrate.ibm.com/> (TDS Orchestrate tenant) and enter your credentials

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/5718eb78-9aab-4557-ba73-a66c7d82d4ac/ascreenshot.jpeg?tl_px=0,202&br_px=1376,971&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=72,277)


20\. Chat with an agent of your choice. Langfuse will monitor all of your interactions with any agent in the activated environment.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/71d6e6ef-4ae5-4aa4-b4b4-580bf9d4b2e0/ascreenshot.jpeg?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=75,-36)


#### Observing Agent Interactions


21\. Once you are done chatting with your agent(s), navigate back to Langfuse and click "Tracing"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-22/4f45f3bc-c723-47ff-bb05-c7ec3eca28b7/user_cropped_screenshot.webp?tl_px=0,172&br_px=1323,911&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=38,189)


22\. This page will show you a table of all traces that Langfuse collected in your environment. Click on one of the traces.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/8165158d-400b-40d6-8824-24313280237f/ascreenshot.jpeg?tl_px=0,58&br_px=1376,827&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=274,277)


23\. Here you can see the preview for the selected trace.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-22/607f9ad5-a73a-4390-bb8b-aaa9d80aae55/user_cropped_screenshot.webp?tl_px=281,86&br_px=1919,1001&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=593,277)


24\. The left panel allows you to explore the depth levels of the trace, or to view all of the observations nested within your selected trace.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-22/22fd2262-f577-4b34-b320-be48f62b706a/user_cropped_screenshot.webp?tl_px=217,142&br_px=1855,1057&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=528,400)


25\. Click on an observation from the left panel.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/65a298a7-1d0c-40f1-a96a-4094b1e5be7a/ascreenshot.jpeg?tl_px=272,206&br_px=1910,1122&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=885,449)


26\. Click here to download the trace data

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/d13173e4-238b-4e2f-bf3f-96d0b975d0d0/user_cropped_screenshot.webp?tl_px=514,157&br_px=1624,777&force_format=jpeg&q=100&width=1110&wat_scale=99&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=433,50)


27\. Click here to structure observations as a timeline

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/a41f8326-7bc0-4620-a07f-25add1974168/user_cropped_screenshot.webp?tl_px=497,143&br_px=1607,763&force_format=jpeg&q=100&width=1110&wat_scale=99&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=512,66)


28\. Click here to change the trace view settings

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/879abe6a-1936-4a16-bf6f-6c7180bc8000/ascreenshot.jpeg?tl_px=415,149&br_px=1525,769&force_format=jpeg&q=100&width=1110&wat_scale=99&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=491,60)


29\. Click here to view a table of observations

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/e44be3c6-e2a3-448d-912b-a39b875aba0c/ascreenshot.jpeg?tl_px=233,154&br_px=1343,774&force_format=jpeg&q=100&width=1110&wat_scale=99&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=114,94)


30\. Click an observation

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/44acbdd6-6d8c-4f56-8527-9209765c3974/ascreenshot.jpeg?tl_px=204,171&br_px=1187,721&force_format=jpeg&q=100&width=983&wat_scale=87&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=352,234)