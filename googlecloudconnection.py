import os
from google.cloud import storage


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:/Users/talha/OneDrive/Desktop/GCP/skilful-alpha-441902-r7-4b7913ba93c5.json'

def create_bucket(bucket_name,storage_class='Standard', location='us-central1'):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = storage_class

    bucket= storage_client.create_bucket(bucket,location=location)

    return f'bucket {bucket_name} successfully created.'

create_bucket('lets_see_this','STANDARD', 'us-central1')

