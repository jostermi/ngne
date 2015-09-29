__author__ = 'cobedien'


import sys
import json
import requests

my_headers = {'content-type': 'application/json-rpc'}
url = "http://192.168.103.3/ins"
username = "admin"
password = "cisco"


payload = [{'jsonrpc': '2.0', 'method': 'cli', 'params': ['show version',1], 'id': '1'}]
my_data = json.dumps(payload)
response = requests.post(url, data=my_data, headers=my_headers, auth=(username, password))


kick_start_image = response.json()['result']['body']['kickstart_ver_str']
system_image = response.json()['result']['body']['kick_file_name']
host_name = response.json()['result']['body']['host_name']

print ("")
print ("===============================")
print ('host name:'+ host_name)
print ('kickstart image version :' + kick_start_image)
print ('system image version :s' + system_image)
print ("===============================")
