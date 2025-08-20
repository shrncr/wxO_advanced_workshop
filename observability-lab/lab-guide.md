# Configuring Langfuse Integration
#### [Made by Sara Hrnciar with Scribe](https://scribehow.com/shared/Configuring_Langfuse_Integration__aRsQFGhcQQGvKJsHxe8h5g)


#### Creating Langfuse Project and Credentials


1\. Navigate to [Langfuse](https://langfuse.com/) and click this button to log in or sign up

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/eab71582-156d-4c84-911e-17b58a8b7c6f/ascreenshot.jpeg?tl_px=544,0&br_px=1920,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=955,121)


2\. Click this button to set up a new Langfuse Organization

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/c45a2744-9ae2-419f-b6c2-944cf4fc517a/user_cropped_screenshot.webp?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=972,109)


3\. Give your organization a name

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/d196f982-36d6-4806-8214-b1b2e5fcb002/ascreenshot.jpeg?tl_px=44,133&br_px=1367,872&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=238,316)


4\. Click "Create"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/bcee0992-d4a6-4948-b1d6-a9e4e1c56464/ascreenshot.jpeg?tl_px=0,289&br_px=1376,1058&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=261,277)


5\. Assign organization members

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/971fdc5d-2c2b-4c5c-98c9-026f515397b8/ascreenshot.jpeg?tl_px=208,240&br_px=1584,1009&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=51,395)


6\. Now you will create a new project within your organization. Name it "orch-observability-lab"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/26a73624-7ab9-44ee-bdcb-9111703974b6/ascreenshot.jpeg?tl_px=20,147&br_px=1396,916&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=219,283)


7\. Click here to create an API Key for your project.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/24d87550-2f72-454c-8cf0-e3037deed134/ascreenshot.jpeg?tl_px=0,123&br_px=1376,892&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=279,277)


8\. Keep This page open. We will need it for the integration.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/f5dd8d6d-8bff-488e-9751-8c45a84501a7/user_cropped_screenshot.webp?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=333,643)


#### Configuring Langfuse Integration with Orchestrate ADK


9\. Open a new terminal

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/69f318fa-ed9a-46bb-a8bb-9b8998e43d2d/ascreenshot.jpeg?tl_px=9,12&br_px=1386,781&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=524,276)


10\. Type the following into the terminal: **orchestrate settings observability langfuse configure --url [https://us.cloud.langfuse.com/api/public/otel](https://us.cloud.langfuse.com/api/public/otel) --health-uri [https://us.cloud.langfuse.com](https://us.cloud.langfuse.com) --project-id**

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/7741245a-7eda-4f81-abe2-955a30dccd45/ascreenshot.jpeg?tl_px=141,0&br_px=1860,961&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=524,193)


11\. Navigate back to the langfuse project page

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/b5db54ca-766d-400b-a2b2-d2bd727bc6b1/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=384,24)


12\. Press [[Ctrl]] + [[C  ]]on this part of the page url to copy the project ID

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/bdb91897-0cbd-43f5-a09a-d5df2d692547/ascreenshot.jpeg?tl_px=0,0&br_px=1919,1073&force_format=jpeg&q=100&width=1120.0)


13\. Press [[Ctrl]] + [[V ]]to paste the project id

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/7c09e3a5-f454-421a-9615-b13dc3375dbd/ascreenshot.jpeg?tl_px=0,126&br_px=1919,1200&force_format=jpeg&q=100&width=1120.0)


14\. type --api-key

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/42a2c378-3723-4079-8d3f-2326eb661c48/ascreenshot.jpeg?tl_px=544,0&br_px=1920,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=955,160)


15\. Go back to Langfuse and copy the **Secret Key**

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/59f0b682-631d-4aec-bcfc-8037a7a6a331/user_cropped_screenshot.webp?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=1025,276)


16\. Paste your Secret Key into the terminal and press [[Return]]

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/786cc81e-3cb4-4a84-9775-6639a1b0bcaf/ascreenshot.jpeg?tl_px=0,126&br_px=1919,1200&force_format=jpeg&q=100&width=1120.0)


17\. Start the Orchestrate server by typing "orchestrate server start -l --env-file=&lt;./relative/path/to/env/file&gt;


18\. Activate the environment for which you'd like to set up observability.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/bd2b0959-6415-4a9f-972d-23547c1f17a5/user_cropped_screenshot.webp?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0)


#### Chat With Agents


19\. Open <https://dl.watson-orchestrate.ibm.com/> (TDS Orchestrate tenant) and enter your credentials

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/5718eb78-9aab-4557-ba73-a66c7d82d4ac/ascreenshot.jpeg?tl_px=0,202&br_px=1376,971&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=72,277)


20\. Chat with an agent of your choice. Langfuse will monitor all of your interactions with any agent in the activated environment.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/71d6e6ef-4ae5-4aa4-b4b4-580bf9d4b2e0/ascreenshot.jpeg?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=75,-36)


#### Observing Agent Interactions


21\. Once you are done chatting with your agent(s), navigate back to Langfuse and click "Tracing"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/920f8091-9ad5-4e23-86c1-d1ece10e50fa/ascreenshot.jpeg?tl_px=0,53&br_px=1376,822&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=35,277)


22\. This page will show you a table of all traces that Langfuse collected in your environment. Click on one of the traces.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/8165158d-400b-40d6-8824-24313280237f/ascreenshot.jpeg?tl_px=0,58&br_px=1376,827&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=274,277)


23\. Here you can see the preview for the selected trace.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/801599ac-caba-4348-ba76-66f7ede4e599/ascreenshot.jpeg?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=665,281)


24\. The left panel allows you to explore the depth levels of the trace, or to view all of the observations nested within your selected trace.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/d3576672-83c4-4e2d-839f-0e1ab6149ae8/ascreenshot.jpeg?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=573,419)


25\. Click on an observation from the left panel.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/65a298a7-1d0c-40f1-a96a-4094b1e5be7a/ascreenshot.jpeg?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=909,498)


26\. Click here to download the trace data

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/d13173e4-238b-4e2f-bf3f-96d0b975d0d0/user_cropped_screenshot.webp?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=538,106)


27\. Click here to structure observations as a timeline

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/a41f8326-7bc0-4620-a07f-25add1974168/user_cropped_screenshot.webp?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=574,106)


28\. Click here to change the trace view settings

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/879abe6a-1936-4a16-bf6f-6c7180bc8000/ascreenshot.jpeg?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=514,107)


29\. Click here to view a table of observations

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/e44be3c6-e2a3-448d-912b-a39b875aba0c/ascreenshot.jpeg?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=188,130)


30\. Click an observation

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/44acbdd6-6d8c-4f56-8527-9209765c3974/ascreenshot.jpeg?tl_px=0,0&br_px=1719,961&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=347,249)


31\. Click here

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-11/2d82a860-028e-4538-935b-66ef7c612c0e/ascreenshot.jpeg?tl_px=0,0&br_px=1920,1200&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=358,444)

