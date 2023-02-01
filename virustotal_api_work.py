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
storage_dict = {"analysis_url": "", "non_clean_verdicts": "", "vendor_verdicts": ""}

# Store URL to dict
try:
    storage_dict["analysis_url"] = url.url
except AttributeError:
    storage_dict["analysis_url"] = "N/A"

# Store malicious verdicts to dict
try:
    # malicious: <integer> number of reports saying that is malicious.
    # suspicious: <integer> number of reports saying that is suspicious.
    # timeout: <integer> number of timeouts when checking this URL.
    # undetected: <integer> number of reports saying that is undetected
    malicious_verdicts_number = (
        url.last_analysis_stats["malicious"]
        + url.last_analysis_stats["suspicious"]
        + url.last_analysis_stats["undetected"]
    )
    storage_dict["malicious_verdicts"] = malicious_verdicts_number
except AttributeError:
    storage_dict["malicious_verdicts"] = "N/A"

# Store providers where analysis is not considered clean
try:
    list_of_values = list(url.last_analysis_results.values())

    engine_dict = []

    for item in list_of_values:
        if item["result"] != "clean":
            engine_dict.append(item["engine_name"])

    storage_dict["vendor_verdicts"] = engine_dict
except AttributeError:
    storage_dict["malicious_verdicts"] = "N/A"

# Convert dictionary object as iterable storage JSON object
json_object = json.dumps(storage_dict, indent=4)
print(json_object)

# file information
# file = client.get_object("/files/44d88612fea8a8f36de82e1278abb02f")
# print(file.get("size"))
