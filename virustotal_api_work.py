import config
import vt

# config key pull
virustotal_key = config.VIRUSTOTAL_KEY

# client API verification
client = vt.Client(virustotal_key)

# URL pull
# get_url = input("Enter URL:")
get_url = "http://wicar.org/"
url_id = vt.url_id(get_url)

# API call
url = client.get_object("/urls/{}", url_id)

# result = client.get_json(analysis)
print(url.last_analysis_stats)

# file information
# file = client.get_object("/files/44d88612fea8a8f36de82e1278abb02f")
# print(file.get("size"))
