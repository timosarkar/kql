# script to get recent detections from abuse.ch API for threat intelligence
import requests
import os
url = "https://mb-api.abuse.ch/api/v1/"

ABUSE_API_KEY = os.getenv("ABUSE_API_KEY")
headers = {
    "Auth-Key": f"{ABUSE_API_KEY}"
}
data = {
    "query": "recent_detections"
}

response = requests.post(url, headers=headers, data=data)
print(response.text)