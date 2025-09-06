# Step 1: Load the connections

## Setup
Prepare by having the following provider API keys handy for cut and paste. The next script will ask for them in sequence. 
- Claude
- Gemini
- OpenAI

Run the set_provider_apikeys.sh script.

Make sure you are in the `ai-gateway-labs` folder so this script is found by your terminal.

```bash
./src/connections/set_provider_apikeys.sh 
```
You can also import the connections as yaml, json, py files. Here is an example of a yaml connection file. This is helpful for more complex connection like ones that involve SSO or OAuth flows. 

```yaml
spec_version: v1
kind: connection
app_id: my_app
environments:
    draft:
        kind: basic
        type: team
        sso: false
        server_url: https://example.com/
    live:
        kind: oauth_auth_on_behalf_of_flow
        type: member
        sso: true
        server_url: https://example.com/
        idp_config:
          header:
            content-type: application/x-www-form-urlencoded
          body:
            requested_token_use: on_behalf_of
            requested_token_type: urn:ietf:params:oauth:token-type:saml2
        app_config:
          header:
            content-type: application/x-www-form-urlencoded
```
You have completed Step 1 of the lab.

Please proceed to [Step 2](../models/README_for_models.md) of the lab