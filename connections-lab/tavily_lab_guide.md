# Tavily Connection Lab - Local ADK
#### [Made by sophia southard with Scribe](https://scribehow.com/shared/Tavily_Connection_Lab_-_Local_ADK__WOf3H21oQtqxnCOwmNl6rw)
This lab shows how to connect watsonx Orchestrate to Tavily, an API for AI-powered web search. By creating and configuring this connection, Orchestrate agents will be able to call Tavily directly for real-time search results. 

1\. Activate virtual environment

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/6ec94fd8-d941-4f8c-86bd-f6c460b9319f/user_cropped_screenshot.png?tl_px=0,0&br_px=905,409&force_format=jpeg&q=100&width=906)



2\. Add connection: 
```bash 
orchestrate connections add --app-id tavily
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/5f6628cd-e863-4c1f-809d-49f294b5dc14/user_cropped_screenshot.png?tl_px=0,0&br_px=1035,205&force_format=jpeg&q=100)


3\. Configure the connection: 
```bash
orchestrate connections configure --app-id tavily --env draft --kind api_key --type team --url \
https://api.tavily.com
```
![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/d113f39c-bbb6-407c-80cf-62dae16df6b1/user_cropped_screenshot.png?tl_px=0,0&br_px=1030,150&force_format=jpeg&q=100)


4\. Add your credentials: 
```bash
orchestrate connections set-credentials --app-id tavily --env draft --api-key <YOUR_API_KEY>
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/19ac7b6a-0f46-4221-8c62-fc5da84b1e7a/user_cropped_screenshot.png?tl_px=0,0&br_px=1054,165&force_format=jpeg&q=100)


5\. Validate: 
```bash
orchestrate connections list
```

![](https://ajeuwbhvhr.cloudimg.io/https://colony-recorder.s3.amazonaws.com/files/2025-08-20/7014d012-cc14-4c59-892d-9543e2bbc9ed/user_cropped_screenshot.png?tl_px=0,0&br_px=848,218&force_format=jpeg&q=100&width=848&wat_scale=75&wat=1&wat_opacity=0.7&wat_gravity=northwest&wat_url=https://colony-recorder.s3.us-west-1.amazonaws.com/images/watermarks/FB923C_standard.png&wat_pad=492,-650)