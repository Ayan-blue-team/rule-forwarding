import requests
import urllib3
urllib3.disable_warnings()

QRADAR_IP = "18.212.3.25"
TOKEN = "57e4bbc2-e588-4577-9904-0bc16beb7793"

HEADERS = {
    "SEC": TOKEN,
    "Version": "12.0",
    "Accept": "application/json"
}

url = f"https://{QRADAR_IP}/api/system/about"
response = requests.get(url, headers=HEADERS, verify=False)
print("Status:", response.status_code)
print("Response:", response.text)
