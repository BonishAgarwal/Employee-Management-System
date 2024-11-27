from app.services.storage.base import StorageService

import boto3
from botocore.exceptions import NoCredentialsError


class AWSStorage(StorageService):
    
    def __init__(self):
        pass
    
    def upload(file_name, bucket, object_name):
        try:
            s3 = boto3.client('s3')
            s3.upload_file(file_name, bucket, object_name)
            print(f"File '{file_name}' uploaded to S3 bucket '{bucket}' successfully.")
        except FileNotFoundError:
            print(f"The file '{file_name}' was not found.")
        except NoCredentialsError:
            print("Credentials not available.")