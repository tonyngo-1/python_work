import requests
import json
import config
import time

# Get urlscan.io key from config file
urlscanio_key = config.URLSCANIO_KEY

# Inititate values outside of try-catch blocks
storage_dict = {}
checked_value_list = []
uuid = ""
uuid_validation = False

# Initiate base URLs
scan_base_url = "https://urlscan.io/api/v1/scan/"
result_base_url = "https://urlscan.io/api/v1/result/"

# Malicious URL Scan
malicious_url = input("Enter malicious URL: \n")

# Header & Data initialization
headers = {"API-Key": urlscanio_key, "Content-Type": "application/json"}
data = {"url": malicious_url, "visibility": "public"}

# Get UUID & validation for UUID existing
while not uuid_validation:
    scan_response = requests.post(scan_base_url, headers=headers, data=json.dumps(data))

    try:
        uuid = scan_response.json()["uuid"]

        uuid_validation = True
    except KeyError:
        num_validation = int(
            input(
                "That didn't work, would you like to re-try a different URL or use our default (https://google.com) by typing 5: \n"
            )
        )

        if num_validation == 5:
            uuid = "6c503e7d-e17e-4ed3-80ed-be780fcd24d8"
            uuid_validation = True


# Grabbing the UUID from the scan_response doesn't work, so it's kinda like a placeholder.
# I'm keeping it there just as a frame of reference to see what the code WOULD look like if the scan works
# If you are able to get to the KeyError for the uuid_validation, the UUID for Google also works
# In the meanwhile, the uuid for linktr.ee is the defualt :^)
uuid = "26f544c9-b869-4ab8-8399-e4a2ae053d20"
result_response = requests.get(
    result_base_url + "%s" % uuid,
    headers=headers,
)

print("Please wait for the results...")
time.sleep(3)

# Get Domain URL
try:
    storage_dict["domain"] = result_response.json()["page"]["domain"]
except KeyError:
    storage_dict["domain"] = "N/A"

# Get Domain ASN
try:
    storage_dict["domain_asn"] = result_response.json()["page"]["asnname"]
except KeyError:
    storage_dict["domain_asn"] = "N/A"

# Get average malicious score from urlscan
try:
    sum_list = [
        result_response.json()["verdicts"]["urlscan"]["score"],
        result_response.json()["verdicts"]["engines"]["score"],
        result_response.json()["verdicts"]["community"]["score"],
    ]

    average_score = round(sum(sum_list) / len(sum_list))

    storage_dict["average_malicious_score"] = average_score
except KeyError:
    storage_dict["average_malicious_score"] = "N/A"

# Get countries where IP is attmepted to be accessed
try:
    for item in result_response.json()["meta"]["processors"]["geoip"]["data"]:

        if not "country_name" in storage_dict:
            storage_dict.setdefault("country_name", []).append(
                item["geoip"]["country_name"]
            )

        add_value = "%s" % item["geoip"]["country_name"]
        checked_value_list = list(storage_dict.values())

        list_to_check = [add_value]

        if not list_to_check in checked_value_list:
            storage_dict["accessed_countries"].append(item["geoip"]["country_name"])
except KeyError:
    storage_dict["accessed_countries"] = "N/A"

print("The resulting dictionary is: \n")
print(storage_dict)
