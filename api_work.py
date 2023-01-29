import time
import requests
import pprint

base_url = "https://analyze.intezer.com/api/v2-0"
response = requests.post(
    base_url + "/get-access-token",
    json={
        "api_key": "35cd0aeb3e663ff96acf3b5c3f4f03973edca329fc5afe67a99e41367a7d2f6c"
    },
)
response.raise_for_status()
session = requests.session()
session.headers["Authorization"] = session.headers["Authorization"] = (
    "Bearer %s" % response.json()["result"]
)

with open("malicious.sample", "rb") as file_to_upload:
    files = {"file": ("file_name", file_to_upload)}
    response = session.post(base_url + "/analyze", files=files)
    assert response.status_code == 201

while response.status_code != 200:
    time.sleep(1)
    result_url = response.json()["result_url"]
    response = session.get(base_url + result_url)
    response.raise_for_status()

report = response.json()
pprint.pprint(report)
