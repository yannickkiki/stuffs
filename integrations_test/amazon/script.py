import os
import boto3

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
AWS_S3_BUCKET_NAME = 'premier-compartiment'
AWS_STATIC_FILES_HOST = f'https://{AWS_S3_BUCKET_NAME}.s3.us-east-2.amazonaws.com/'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def upload_to_aws(file_name):
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

    file_location = BASE_DIR + '/' + file_name
    s3_file_name = file_name

    s3.upload_file(file_location, AWS_S3_BUCKET_NAME, s3_file_name)

    file_url = AWS_STATIC_FILES_HOST + s3_file_name
    return file_url


upload_to_aws(file_name='sample_filee.png')
