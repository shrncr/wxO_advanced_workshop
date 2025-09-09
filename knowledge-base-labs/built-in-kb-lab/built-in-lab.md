# Creating a Built-in Milvus Vector Database with Custom Embedding-Model and Parameters

##### Introduction

In this lab, we will walk through creating a knowledge base using the built-in Milvus vector database that comes with Orchestrate. The built-in knowledge base that comes with WxO is a huge differentiator. Vector Databases are expesive, so this lab is focusing on getting the most out of the built-in database that comes with WxO. 

To help increase the accuracy of our built-in vector db, in this lab, you will learn how to change the embedding model and configure parameters that are not currently documented such as chunk size and chunk overlap. Without the ability to change these parameters, our standard search configurations may not contain all the information to answer a customer's question. An example of where this may come into play would be a document with sections on certain topics, such as a wikipedia page. 

These features are currently only available in the ADK, so any advanced configurations of your knowledge base has to be done here!

Note: The commands in this lab are based in the lab folder, you may have to cd into the lab folder to perfom these actions.

##### Activating Our Environment

```
Orchestrate env activate #YourEnvName
```

1\. The first thing that we will do is activate our environment from IBM Cloud. Copy the line of code from above and enter your environment name then click enter.

If prompted, paste in your API key details.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/e2678fb2-ae7b-4e5d-8aae-97b28dcb2df9/ascreenshot.jpeg?tl_px=195,466&br_px=1000,915&force_format=jpeg&q=100&width=804)

##### Knowledge Base Configuration

2\. Next, we are going to take a look at our knowledge base settings.

Open the Builtin.yaml file

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/9d599387-dc94-49d3-be64-4865f5501b07/user_cropped_screenshot.webp?tl_px=0,134&br_px=502,415&force_format=jpeg&q=100&width=503)

3\. Here, you will have to change this path to the location where your document is located.

On this page, you can also see the embedding model that we will be using, as well as some areas where you can change some parameters such as chunk size and chunk overlap.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/849ae0cd-b00e-45c9-93de-879c5c37732a/ascreenshot.jpeg?tl_px=230,70&br_px=1091,551&force_format=jpeg&q=100&width=860&wat_scale=76&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=617,120)

```
 orchestrate knowledge-bases import -f Builtin.yaml
```

4\. Back in the Terminal, we will be importing our knowledge base.

Copy the line of code from above and paste it into your terminal.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/1d6dd928-90d3-46ae-bab2-5000f71022cb/ascreenshot.jpeg?tl_px=217,493&br_px=1021,943&force_format=jpeg&q=100&width=804)

```
orchestrate knowledge-bases status --name F1Knowledge
```

5\. Now that our knowledge base has been imported, that does not mean that it was indexed correctly. To check this, use the line of code from above and  paste that into your terminal.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/740e9d4e-4ff8-419e-b424-7efb53182082/ascreenshot.jpeg?tl_px=182,509&br_px=987,958&force_format=jpeg&q=100&width=804)

6\. Review that your knowledge base has indexed correctly and is in the "Ready" status.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/f59aea03-9f12-4e11-b4da-ad00cde92617/ascreenshot.jpeg?tl_px=506,439&br_px=1653,1080&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=523,360)

##### Agent Configuration

7\. Next we are going to be opening our F1Agent.yaml File.


8\. Review the agent configuration.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/07f7a3c6-1656-4d1d-893d-33c96486111f/ascreenshot.jpeg?tl_px=244,60&br_px=1104,541&force_format=jpeg&q=100&width=860&wat_scale=76&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=431,135)

```
orchestrate agents import -f F1Agent.yaml
```

9\. It is now time to import our agent with the knowledge base attached,

Head back to your terminal and copy and paste the line of code above.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/3caac8d4-cebb-4d06-b0c7-3b1487638161/ascreenshot.jpeg?tl_px=217,596&br_px=1021,1045&force_format=jpeg&q=100&width=804)

##### Testing

10\. Once that has ran correctly, we will be heading into our IBM Cloud instance of Watsonx Orchestrate and then open the hamburger menu.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/b57dad8c-57e5-4a2b-8608-eea591074857/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=-19,51)

11\. Head to the Agent Builder Section on the left hand side

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/e5dac22a-f235-4d0e-b58c-b9063afc2828/ascreenshot.jpeg?tl_px=0,0&br_px=1376,769&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=77,168)

12\. Click on the RacingHistory Agent to open the details.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/452157e8-34bc-4f26-bba3-c37496b0a314/ascreenshot.jpeg?tl_px=142,413&br_px=1125,962&force_format=jpeg&q=100&width=983&wat_scale=87&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=459,243)

13\. If you scroll down to the knowledge section, we can see that our F1Hist.pdf is uploaded.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/f6424dcc-4dec-4e7f-92aa-f4d0eccba5a5/ascreenshot.jpeg?tl_px=411,393&br_px=1271,873&force_format=jpeg&q=100&width=860&wat_scale=76&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=161,215)

14\. Head into the preview section and type in "Who won the first F1 Race"

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/1c18bf89-e5ce-4813-a0a6-f3383d95b44d/ascreenshot.jpeg?tl_px=1184,310&br_px=2560,1080&force_format=jpeg&q=100&width=1120.0&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=321,572)

15\. You can review the response here. You may see that our agent is responding like it is an announcer, we were able to direct it to that in the behavior section.

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/5575b0bf-aba4-4058-b66d-5318409780b7/ascreenshot.jpeg?tl_px=1548,188&br_px=2531,738&force_format=jpeg&q=100&width=983&wat_scale=87&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=312,311)

16\. Here in the behavior section, we can see how our agent responds, feel free to change this and test out the agent that you just built!

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-09-03/4b92c08d-b6f8-4317-a3aa-ec8029b06ab8/ascreenshot.jpeg?tl_px=382,356&br_px=1147,783&force_format=jpeg&q=100&width=764&wat_scale=68&wat=1&wat_opacity=1&wat_gravity=northwest&wat_url=https://colony-recorder.s3.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=336,190)

##### Conclusion

You have now completed this lab! In this lab, we learned how to import a built-in knowledge base with a new embedding model!

We also learned that we can change some parameters in the ADK that are currently unchangeable in the UI, such as Chunk Size, Chunk Overlap, and the embedding model itself.

I hope you enjoyed this lab and please reach out if you have any questions!
