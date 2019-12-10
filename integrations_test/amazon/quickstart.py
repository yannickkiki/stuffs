import os
import boto3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

s3 = boto3.resource('s3')

data = open(BASE_DIR + '/' + 'sample_filee.png', 'rb')
s3.Bucket('premier-compartiment').put_object(Key='sample_filee.png', Body=data)
