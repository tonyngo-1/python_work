import time
import config
import requests

intezer_key = config.INTEZER_KEY

base_url = "https://analyze.intezer.com/api/v2-0"

# API URL setup with key using requests library
response = requests.post(
    base_url + "/get-access-token",
    json={"api_key": intezer_key},
)

# API authentication
response.raise_for_status()
session = requests.session()
session.headers["Authorization"] = session.headers["Authorization"] = (
    "Bearer %s" % response.json()["result"]
)

# Malicious URL Scan
malicious_url = input("Enter malicious URL: ")
malicious_url = "google.com"
params = {"url": malicious_url}
response = requests.post(
    base_url + "/get-access-token", json={"api_key": "YOUR API KEY"}
)
response = session.post(base_url + "/url", params=params)
response = session.post(
    "https://analyze.intezer.com/api/v2-0/url", params={"url": "https://intezer.com"}
)


# Malicious URL Scan Result
verdict = "491367cc-295b-45bb-821f-5fc667720ef6"
params = {"analysis_id*": verdict}
response = session.get(base_url + "/url/%s" % verdict)

print(response.json())
