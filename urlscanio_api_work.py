import requests
import json
import config

urlscanio_key = config.URLSCANIO_KEY

storage_dict = {}
checked_value_list = []


scan_base_url = "https://urlscan.io/api/v1/scan/"
result_base_url = "https://urlscan.io/api/v1/result/"
# Malicious URL Scan
# malicious_url = input("Enter malicious URL: ")
# malicious_url = "google.com"

headers = {"API-Key": urlscanio_key, "Content-Type": "application/json"}
# data = {"url": malicious_url, "visibility": "public"}
# response = requests.post(base_url, headers=headers, data=json.dumps(data))


uuid = "6c503e7d-e17e-4ed3-80ed-be780fcd24d8"

response = requests.get(
    result_base_url + "%s" % uuid,
    headers=headers,
)


sum_list = [
    response.json()["verdicts"]["urlscan"]["score"],
    response.json()["verdicts"]["engines"]["score"],
    response.json()["verdicts"]["community"]["score"],
]

average_score = round(sum(sum_list) / len(sum_list))

print(average_score)

storage_dict["average_malicious_score"] = average_score


for item in response.json()["meta"]["processors"]["geoip"]["data"]:

    if not "country_name" in storage_dict:
        storage_dict.setdefault("country_name", []).append(
            item["geoip"]["country_name"]
        )

    add_value = "%s" % item["geoip"]["country_name"]
    checked_value_list = list(storage_dict.values())

    asdasd = [add_value]

    if not asdasd in checked_value_list:
        storage_dict["country_name"].append(item["geoip"]["country_name"])

print(storage_dict)
