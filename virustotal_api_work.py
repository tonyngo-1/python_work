import config
import vt
import json

# config key pull
virustotal_key = config.VIRUSTOTAL_KEY

# client API verification
client = vt.Client(virustotal_key)

# URL pull
# get_url = input("Enter URL:")
get_url = "http://google.com/"
url_id = vt.url_id(get_url)

# API call
url = client.get_object("/urls/{}", url_id)

# Initialize dictionary
storage_dict = {"url": "", "malicious_verdicts": "", "vendor_verdicts": ""}

# Store URL to dict
storage_dict["url"] = url.url

# Store malicious verdicts to dict
storage_dict["malicious_verdicts"] = url.last_analysis_stats["malicious"]

# Store providers where analysis is not considered clean
list_of_values = list(url.last_analysis_results.values())

engine_dict = []

for item in list_of_values:
    if item["result"] != "clean":
        engine_dict.append(item["engine_name"])

storage_dict["vendor_verdicts"] = engine_dict

# print("dictionary print:")
# print(storage_dict)

json_object = json.dumps(storage_dict, indent=4)
# print(json_object)

print("json print:")
print(json_object)
# print(engine_dict)
# Store nested dictionary results
# print(list(url.last_analysis_results.values()))
# {'category': 'harmless', 'result': 'clean', 'method': 'blacklist', 'engine_name': 'PhishFort'}
# if category == "suspicious" or "maicious"
#   take result, and store in dictionary


# print(url.last_analysis_results["jj"]["category"])
#

# new_dict = url.last_analysis_results.values()
# value_list=list(dict.values())
# print(list(new_dict["category"]))
# print(
#     list(url.last_analysis_results.keys())[
#         list(url.last_analysis_results.values()).index("Bkav")
#     ]
# )
# print(
#     list(url.last_analysis_results.keys())[
#         list(url.last_analysis_results.values()).index("clean")
#     ]
# )

# Store description to verdict

# storage_dict.append(url.url)
# print(storage_dict)


# json_object = json.dumps(url.last_analysis_stats, indent=4)
# print(json_object)

# file information
# file = client.get_object("/files/44d88612fea8a8f36de82e1278abb02f")
# print(file.get("size"))
