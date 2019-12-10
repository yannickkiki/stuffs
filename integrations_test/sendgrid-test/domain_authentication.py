import json
import requests

# https://sendgrid.api-docs.io/v3.0/domain-authentication/list-all-authenticated-domains
url = "https://api.sendgrid.com/v3/whitelabel/domains"
headers = {
    'authorization': "xxx",
}

# List all authenticated domains
payload = {}
response = requests.request("GET", url, data=json.dumps(payload), headers=headers)
data_1 = response.json()

# Authenticate a domain
payload = {
    "domain": "almeki.tech",
    "subdomain": "foxx"
}
headers.update({'content-type': 'application/json'})
response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
data_2 = response.json()

# Verify domain authentication
url = f"https://api.sendgrid.com/v3/whitelabel/domains/{data_2['id']}/validate"
response = requests.request("POST", url, headers=headers)
data_3 = response.json()
