import time
import config
import requests

intezer_key = config.INTEZER_KEY
virustotal_key = config.VIRUSTOTAL_KEY

# base url setup
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
params = {"url": malicious_url}
response = session.post(base_url + "/url", params=params)

# Malicious URL Scan Result
verdict = "/url/0833e33b-2dcd-4d48-a853-8b4822675911"


print(response.json())

# Malicious File upload
# with open("malicious.sample", "rb") as file_to_upload:
#     files = {"file": ("file_name", file_to_upload)}
#     response = session.post(base_url + "/analyze", files=files)
#     assert response.status_code == 201

# I
# while response.status_code != 200:
#     time.sleep(1)
#     result_url = response.json()["result_url"]
#     response = session.get(base_url + result_url)
#     response.raise_for_status()

# report = response.json()
# print(report)
# # pprint.pprint(report)
