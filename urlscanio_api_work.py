import requests
import json
import config

urlscanio_key = config.URLSCANIO_KEY

base_url = "https://urlscan.io/api/v1/scan/"

# Malicious URL Scan
# malicious_url = input("Enter malicious URL: ")

# malicious_url = "google.com"
headers = {"API-Key": urlscanio_key, "Content-Type": "application/json"}
# data = {"url": malicious_url, "visibility": "public"}
# response = requests.post(base_url, headers=headers, data=json.dumps(data))
# uuid = ""

# try:
#     uuid = response.json()["uuid"]
# except KeyError:
#     uuid = "6c503e7d-e17e-4ed3-80ed-be780fcd24d8"

response = requests.get(
    "https://urlscan.io/screenshots/6c503e7d-e17e-4ed3-80ed-be780fcd24d8.png",
    headers=headers,
)
print(response.json())
# print(uuid)
# if uuid != "":
#

#     print(response.json())

# response_tojson = response.json()
# iterable_json = json.loads(response_tojson)
# print(iterable_json)
# try:

#     print(uiud)

# except AttributeError:
#     uiud = "N/A"


# print(response)
# print(response.json())

# import requests
# import json

# headers = {
#     "API-Key": "5c246f3c-3d26-4ae6-bdb5-9165611f69bd",
#     "Content-Type": "application/json",
# }
# data = {"url": "https://urlyouwanttoscan.com/path/", "visibility": "public"}
# response = requests.post(
#     "https://urlscan.io/api/v1/scan/", headers=headers, data=json.dumps(data)
# )
# print(response)
# print(response.json())
