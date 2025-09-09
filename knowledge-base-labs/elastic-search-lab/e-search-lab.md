# Connecting an ElasticSearch instance to WxO Knowledge Using the ADK

##### Introduction

In this lab, we will be connecting an external Elasticsearch instance as our knowledge base through the ADK. ElasticSearch has a number of great benefits including webcrawlers, advanced search parameters, and it can handle a large amount of documents for Enterprise use cases. The advanced search parameters can greatly improve the capability to return the right chunk from the correct document (Think law use cases where documents are structured the same, but we may need ES to find the correct case in the file name, and then search that document for our answer.)

Note: The commands in this lab are based in the lab folder, you may have to cd into the lab folder to perfom these actions.

Note: The Wikipedia knowledge is in this folder for your information, it has already been uploaded into the knowledge base.

##### Configuring our Connection

```
Orchestrate env activate YourEnvName
```

1\. The first thing we are going to do is activate our IBM Cloud instance. Copy the code above and insert your environment name before pasting in the terminal. Paste your API key in if prompted.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/8f5ca3c5-72f7-45f5-8b7c-21d3737dbc6a/user_cropped_screenshot.webp?tl_px=202,439&br_px=846,799&force_format=jpeg&q=100&width=644)

```
orchestrate connections add --app-id my_Esearch_conn
```

2\. Next, we will be creating our Connection that will connect to ElasticSearch. Copy the line of code above and paste into your terminal.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/ea302c49-4d2b-446f-96c9-3fca9c3140d3/user_cropped_screenshot.webp?tl_px=235,465&br_px=945,862&force_format=jpeg&q=100&width=710)

```
orchestrate connections configure --app-id my_Esearch_conn --environment draft --kind basic --type team --server-url https://YOURSERVERURL.com
```

3\. Next, we need to configure our connection by adding our server-url, paste the server url from your instructor into the line of code above and then enter it into your terminal.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/fd77286d-7ed1-4bff-8653-98efea324178/user_cropped_screenshot.webp?tl_px=426,509&br_px=1136,906&force_format=jpeg&q=100&width=710)

```
orchestrate connections set-credentials --app-id my_Esearch_conn --environment draft -u USERNAME -p PASSWORD
```

4\. Next, we need to add our username and password for the credentials. Copy the username and password from your instructor into the line above and enter into your terminal.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/d2b73366-fe4e-420a-8a99-1d551407a6f0/user_cropped_screenshot.webp?tl_px=400,590&br_px=1044,950&force_format=jpeg&q=100&width=644)

##### Knowledge Base Configuration

5\. Next, we will be opening our ES.yaml file to look at the knowledge base configuration.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/467b15a8-5b3d-4f12-b6b6-02b18275c3ec/user_cropped_screenshot.webp?tl_px=0,134&br_px=542,437&force_format=jpeg&q=100&width=542)

6\. You will have to use the URL from earlier in this lab that was provided by your instructor to paste into this line. Save the file after you have made that change.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/5aeeefe8-9e63-4714-af7a-cf3421dcfdb7/user_cropped_screenshot.webp?tl_px=229,38&br_px=1021,480&force_format=jpeg&q=100&width=792)

```
orchestrate knowledge-bases import -f ES.yaml -a my_Esearch_conn
```

7\. Next, we will be importing our knowledge base and associating it with our connection. Copy the line from above and enter it into your terminal.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/f7dc31f9-b7db-4203-a50f-8361e98a2440/user_cropped_screenshot.webp?tl_px=238,518&br_px=1030,961&force_format=jpeg&q=100&width=792)

```
orchestrate knowledge-bases status --name Esearch
```

8\. We will now be checking the status of the knowledge base by using the line above. Copy and paste that into your terminal.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/03fad90b-629f-47cf-8aa6-cac274578896/user_cropped_screenshot.webp?tl_px=179,498&br_px=971,940&force_format=jpeg&q=100&width=792)

9\. Now we can confirm that our index is ready and is conncted.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/4c62852a-9916-40df-b8f1-8bd6577633ea/user_cropped_screenshot.webp?tl_px=849,683&br_px=1559,1080&force_format=jpeg&q=100&width=710&wat_scale=63&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=444,197)

##### Importing and Testing our Agent

```
orchestrate agents import -f ESAgent.yaml -a my_Esearch_conn
```

10\. Next, we will be importing our agent using the line of code above. Paste that into your terminal.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/85d3607d-dee9-41f2-94cc-e63a189fd8ea/user_cropped_screenshot.webp?tl_px=287,683&br_px=997,1080&force_format=jpeg&q=100&width=710)

11\. Now that our agent has been imported successfully, we can move into our IBM Cloud environment to test it.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/62b1c984-aaf6-4b40-8137-490a87627e25/user_cropped_screenshot.webp?tl_px=204,750&br_px=793,1080&force_format=jpeg&q=100&width=589)

12\. Click the hamburger menu in Watson Orchestrate

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/f64a9db6-579c-4f92-a1b2-1e01d2e35083/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=-22,81)

13\. And then click on the Agent Builder Tile.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/f2598d2b-adad-4a0d-9caf-046b952dd29c/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=94,195)

14\. Click on the Ferrari Agent that you just created.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/e58f432b-4bd0-4e46-952e-6d7f58f2a508/ascreenshot.jpeg?tl_px=0,254&br_px=1376,1023&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=456,277)

15\. If we scroll down, we can see that Elasticsearch has been configured correctly.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/10440a22-9ac3-426a-8725-1454642f02b4/ascreenshot.jpeg?tl_px=0,310&br_px=1376,1080&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=289,369)

16\. Click the preview tile and ask **"Tell me about Ferrari's History"**

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/249801f5-ed0c-4ba8-9462-dcf23ca31d37/ascreenshot.jpeg?tl_px=1252,439&br_px=2399,1080&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=346,562)

17\. Review the response from our agent and hit this dropdown to view the sources.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/2c87d5d8-8f6f-4b3f-b114-d945eea5f600/ascreenshot.jpeg?tl_px=1413,259&br_px=2560,900&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=906,299)

18\. Flip through the sources to see where the information came from in the article that was fed into ElasticSearch.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/5f7462e8-ab73-417f-816b-d58fd50d06b1/ascreenshot.jpeg?tl_px=1184,310&br_px=2560,1080&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=760,383)

##### Conclusion

This is the end of the lab. In this lab we connected an ElasticSearch instance to WxO as an external knowledge base. ElasticSearch has a ton of extra configurations that we did not get into today, I highly recommend looking at some of the configurations on [this page.](https://github.com/watson-developer-cloud/assistant-toolkit/blob/master/integrations/extensions/docs/elasticsearch-install-and-setup/how_to_configure_advanced_elasticsearch_settings.md) This page also walks through using Webcrawlers and some other features we did not touch today. Hope you enjoyed this section and reach out if you have any questions!

For this lab, I configured the Elasticsearch index, if you want to recreate that, there are some rough steps below

- Reserve a techzone instance of watsonxdiscovery (must have platinum node for RAG)
- Connect Watsonx.discovery/Elasticsearch to watsonx.ai
- Create a vector index using ElasticSearch
- Use your credentials as replacements for the ones in this lab.
