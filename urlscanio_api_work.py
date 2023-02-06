import requests

# urlscanio_key = config.URLSCANIO_KEY
urlscanio_key = "5c246f3c-3d26-4ae6-bdb5-9165611f69bd"

base_url = "https://urlscan.io/api/v1/scan/"

# Malicious URL Scan
# malicious_url = input("Enter malicious URL: ")
malicious_url = "https:google.com"
headers = {"API-Key": urlscanio_key, "Content-Type": "application/json"}
params = {"url": malicious_url, "visiblity": "public"}
response = requests.post(base_url, headers=headers, params=params)

# print(response)
print(response.json())

# import requests
# import json
# headers = {'API-Key':'$apikey','Content-Type':'application/json'}
# data = {"url": "https://urlyouwanttoscan.com/path/", "visibility": "public"}
# response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
# print(response)
# print(response.json())
