orchestrate server start 
orchestrate env activate local

orchestrate connections add --app-id tavily 
orchestrate connections configure --app-id tavily --env draft --type member --kind api_key
orchestrate orchestrate connections set-credentials --app-id tavily --env draft -k <put-key-here>

orchestrate connections add --app-id gmail
orchestrate connections configure --app-id gmail --env draft --type member --kind basic
orchestrate connections set-credentials --app-id gmail --env draft -u <youremail> -p <your app password, should look like xxxx xxxx xxxx xxxx>

orchestrate tools import -k python -f ./tools/web_search.py --app-id tavily 
orchestrate tools import -k python -f ./tools/gmail.py --app-id gmail
orchestrate tools import -k flow -f ./tools/flow.py

orchestrate agents import -f ./agents/agent.yaml

