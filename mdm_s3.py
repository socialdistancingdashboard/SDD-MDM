import os
import boto3
from datetime import datetime

directory = r'/tmp'
for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            print(os.path.join(directory, filename))
            s3 = boto3.resource('s3')
            s3.Bucket('sdd-s3-bucket').upload_file(os.path.join(directory, filename), f"mdm/{datetime.now().strftime('%Y/%m/%d/%H')}" + "/" + filename)  
        else:
            continue
