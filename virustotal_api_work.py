import config
import vt

# config key pull
virustotal_key = config.VIRUSTOTAL_KEY

# client API verification
client = vt.Client(virustotal_key)

# URL pull
# get_url = input("Enter URL:")
get_url = "google.com"

# analysis
analysis = client.scan_url(get_url)

# file information
# file = client.get_object("/files/44d88612fea8a8f36de82e1278abb02f")
# print(file.get("size"))