# Prerequisities:
- You have a GitHub Personal Access Token with package read access
- You are connected to the VPN (required to access OpenShift)

# Steps:
1. Login to OpenShift web console
2. Profile -> "copy login command"
3. Copy login command, paste to terminal
4. Ensure that you're in the project where you want to deploy (ex. int02, etc). Switch by using `oc project <project name>`
5. Create image pull secret:
`oc create secret docker-registry <pull_secret_name> --docker-server=ghcr.io --docker-username=docker --docker-password=<GitHub PAT>`
6. 
