import http.client
import json
import ssl
import os
import gzip
import io
from datetime import datetime

api_key = os.environ["mdm_key"]
 
# Defining certificate related stuff and host of endpoint
certificate_file = 'mdm.pem'
certificate_secret = api_key
host = 'broker.mdm-portal.de'
 
# Defining parts of the HTTP request
request_url='/BASt-MDM-Interface/srv/3717000/clientPullService?subscriptionID=3717000'
request_headers = {
    'Content-Type': 'text/xml'
}
 
# Define the client certificate settings for https connection
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_cert_chain(certfile=certificate_file, password=certificate_secret)
 
# Create a connection to submit HTTP requests
connection = http.client.HTTPSConnection(host, port=443, context=context)
 
# Use connection to submit a HTTP POST request
connection.request(method="GET", url=request_url, headers=request_headers)
 
# Print the HTTP response from the IOT service endpoint
response = connection.getresponse()
print(response.status, response.reason)
data = response.read()
compressed_data = io.BytesIO(data)
f = open("/tmp/3717000.xml", "w")
for data in gzip.GzipFile(fileobj=compressed_data):
    f.write(str(data,'utf-8'))  
f.close()