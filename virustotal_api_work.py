import config
import vt
import json

# config key pull
virustotal_key = config.VIRUSTOTAL_KEY

# client API verification
client = vt.Client(virustotal_key)

# Begin loop
while True:
    # user_input = input("1: Scan a URL, 2: Scan a file, 3: exit\n")
    user_input = "2"
    if user_input == "1":
        # URL pull
        # get_url = input("Enter URL:")
        get_url = "http://google.com/"
        url_id = vt.url_id(get_url)

        # API call
        url = client.get_object("/urls/{}", url_id)

        # Initialize dictionary
        storage_dict = []

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

        print("URL %s will be added to the database" % storage_dict["analysis_url"])
        # print(json_object)

    elif user_input == "2":
        # print("this will be for file scanning, sha ")

        # Get File Object (SHA-1 hash)
        file = client.get_object("/files/5767653494d05b3f3f38f1662a63335d09ae6489")

        print(file.md5)

        # print(file)

        # with open("/Users/tony/Desktop/eicar2.com", "rb") as f:
        #     analysis = client.scan_file(f, wait_for_completion=True)
        break

    elif user_input == "3":
        print("goodbye")
        break

    else:
        print("invalid input, try again")
