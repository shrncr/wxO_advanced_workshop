# Connecting a Milvus Vector Database from Watsonx.Data to WxO using the ADK

###### Introduction

In this lab, we will be connecting a Milvus VectorDatabase from Watsonx.data into WxO to use as a knowledge source for one of our agents.

Note: The commands in this lab are based in the lab folder, you may have to cd into the lab folder to perfom these actions.

Note: The Wikipedia knowledge is in this folder for your information, it has already been uploaded into the knowledge base.

##### Configuring our Connection

```
orchestrate env activate #YourEnvironmentName
```

###### 1. First, we need to activate our environment in ibm cloud

Copy the line from above and Enter your Environment name and hit enter.

Then, paste your IBM Cloud API Key and then hit enter.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/c7374f37-b1f8-4a0a-886d-ed292c5bb44d/user_cropped_screenshot.webp?tl_px=200,31&br_px=910,428&force_format=jpeg&q=100&width=710)

```
orchestrate connections add --app-id my_milvus_conn
```

###### 2\. Paste in the line of code from above and click Enter.

This line is creating our connection to Milvus that we will use for our knowledge base.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/e4897731-c14b-4a96-bdc1-10ab62354433/user_cropped_screenshot.webp?tl_px=226,180&br_px=946,583&force_format=jpeg&q=100)

```
orchestrate connections configure --app-id my_milvus_conn --environment draft --kind basic --type team --server-url #EnterinServerURLHere
```

###### 3\. Next, you need to add the Server URL from your instructor into the line of code above and hit enter.

This line of code is configuring our connection that we just created.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/fb85096a-e5cb-4933-89c6-cc33c3e5cd69/user_cropped_screenshot.webp?tl_px=213,135&br_px=1017,585&force_format=jpeg&q=100&width=804)

```
orchestrate connections set-credentials --app-id my_milvus_conn --environment draft -u ibmlhapikey -p #PASSWORD
```

###### 4\. Next, you will need to get add the password from the instructor into the line of code above and hit enter.

This line is setting the credentials for our connection.

![img](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/23a89ada-831e-4557-86bc-52786e9d73f1/user_cropped_screenshot.webp?tl_px=225,241&br_px=1029,691&force_format=jpeg&q=100&width=804)\

##### Configuring out Knowledge Base

###### 5\. Click on the MilvusF1.yaml file

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/d1d6207f-86b1-4a43-8768-9229a07ea68e/user_cropped_screenshot.webp?tl_px=28,137&br_px=616,466&force_format=jpeg&q=100&width=589&wat_scale=52&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=95,173)

###### 6\. Review the Connection Details and Knowledge base configurations for this Knowledge Base.

- Copy and Paste the GRPC_Host URL and the GRPC_ Port from your instructor into this file and Save your file.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/0d917f96-9129-423a-9adb-2f1c4d4da4cf/user_cropped_screenshot.webp?tl_px=253,68&br_px=963,465&force_format=jpeg&q=100&width=710&wat_scale=63&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=224,173)

```
orchestrate knowledge-bases import -f MilvusF1.yaml -a my_milvus_conn
```

###### 7\. Head back to your terminal and Paste in the line from above and hit Enter.

This line is creating knowledge base and associating it with the connection that we made a few steps ago.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/abf176b1-6303-4435-b6b5-dedc477203ff/user_cropped_screenshot.webp?tl_px=244,213&br_px=1048,662&force_format=jpeg&q=100&width=804)

```
orchestrate knowledge-bases status --name ibm_knowledge_F1
```

###### 8\. Next we are going to view the status of our knowledge base. This is a great way to see if your knowledge base was provisioned correctly. Paste in the line from Above and Hit Enter.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/ac55d593-d1ac-475e-8c77-0f85f2f4cd28/user_cropped_screenshot.webp?tl_px=217,290&br_px=1021,740&force_format=jpeg&q=100&width=804)

###### 9\. Review the "Ready and the "Connection ID" tabs to make sure your knowledge base was connected correctly, if you are having issues with your knowledge bases, check here first!

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/0c6e6d73-ab71-47fb-9a66-67726c44b1fe/user_cropped_screenshot.webp?tl_px=867,292&br_px=1659,735&force_format=jpeg&q=100&width=792&wat_scale=70&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=249,118)

Tip: If your environment was not configured correctly in the previous step, it may be due to a bug that was fixed in ADK version 1.10, where changes to knowledge bases may delete the connection. To fix this, please delete your knowledge base and re-import it.

##### Importing and Testing Agent

```
orchestrate agents import -f Milvusagent.yaml -a my_milvus_conn
```

###### 10\. Next, we are going to import our agent into our SaaS instance. Copy the line from above into your Terminal and hit enter.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/ea51d691-c6ce-4d46-8c3d-4cc33619b23c/user_cropped_screenshot.webp?tl_px=215,369&br_px=1110,869&force_format=jpeg&q=100&width=895)

###### 11\. Head to your homepage of your Watsonx Orchestrate instance and click on the Build tile.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/572760ab-635e-417d-986c-4a7c5dba0bcf/user_cropped_screenshot.webp?tl_px=0,0&br_px=894,501&force_format=jpeg&q=100&width=895&wat_scale=79&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=178,221)

###### 12\. Click on the "Agent Builder"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/9a48e6ad-7e93-42d1-8b6a-ae36db64b207/user_cropped_screenshot.webp?tl_px=0,62&br_px=791,505&force_format=jpeg&q=100&width=792&wat_scale=70&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=96,195)

###### 13\. Click on your agent that was just created. (yours will be named F1 Movie Agent)

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/cbfbca69-67dc-4a83-bb9b-f7bba4a86c62/user_cropped_screenshot.webp?tl_px=0,0&br_px=2560,1080&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=218,235)

###### 14\. Scroll down to the knowledge section and you can see that Milvus was configured.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/d6e68fbd-73db-4669-b9d8-187ba3035f47/user_cropped_screenshot.webp?tl_px=396,308&br_px=1425,883&force_format=jpeg&q=100&width=1029&wat_scale=91&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=75,294)

###### 15\. Head to the search bar and type in "What happened in the F1 movie" (sorry for any spoilers)

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/95cceae3-d7f5-4e5d-a636-b802ac9b8661/ascreenshot.jpeg?tl_px=1184,310&br_px=2560,1080&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=355,571)

###### 16\. Click on the dropdown button from the response

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/57aa84b3-b68b-427b-a69f-a753da3bb009/ascreenshot.jpeg?tl_px=1413,218&br_px=2560,859&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=399,184)

###### 17\. Click on View Source

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/a8aca887-e2d7-44aa-9458-a8e1024b920d/ascreenshot.jpeg?tl_px=1413,164&br_px=2560,805&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=176,415)

###### 18\. Here you can see the source where the result was pulled from. This comes from a chunk in our Milvus vector database.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-02/38a3b563-e76e-45a3-9572-9026849a3bea/ascreenshot.jpeg?tl_px=1033,91&br_px=2016,640&force_format=jpeg&q=100&width=983&wat_scale=87&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=459,243)

##### Conclusion

You have now completed this lab! In this lab we learned how to connect an external Milvus database to WxO through the ADK! I hope you enjoyed this section and please reach out if you have any questions!

If you are interested in recreating the vector Database with Milvus in the future, there are some rough steps below:

1. Have a techzone reservation that includes Watsonx.data, Cloud Object Storage, and Watsonx.ai
2. Configure Watsonx.Data
3. Create and Connect COS Bucket
4. Create a Milvus Engine in Watsonx.data (takes a while to provision)
5. Connect Milvus to Watsonx.ai
6. Create Vector Index in Watsonx.ai
7. Use Vector index and Milvus Credentials to replace the values in this lab
