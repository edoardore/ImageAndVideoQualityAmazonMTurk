import boto3
from botocore.exceptions import NoCredentialsError
import os
import pickle

aws_access_key_id = ''
aws_secret_access_key = ''


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      )
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful of " + s3_file)
        return True
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploaded = []
images = os.listdir("images")
len = len(images)
i = 0
for img in images:
    if upload_to_aws("images/" + img, 'imagesformturk', img):
        i += 1
        uploaded.append("https://imagesformturk.s3.eu-central-1.amazonaws.com/" + img)
        percent = str(i * 100 / len)
        print (percent + '%')
pickle.dump(uploaded, open('imagesurl.p', 'wb'))
