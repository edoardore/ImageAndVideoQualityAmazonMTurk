import boto3
from botocore.exceptions import NoCredentialsError
import os
import pickle
import mimetypes
import Key


def getImg():
    aws_access_key_id = Key.getAws_access_key_id()
    aws_secret_access_key = Key.getAws_secret_access_key()

    def upload_to_aws(local_file, bucket, s3_file):
        s3 = boto3.client('s3',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          )
        try:
            s3.upload_file(local_file, bucket, s3_file,
                           ExtraArgs={"ContentType": mimetypes.MimeTypes().guess_type(s3_file)[0]})

            print("Upload Successful of " + s3_file)
            return True

        except NoCredentialsError:
            print("Credentials not available")
            return False

    try:
        uploaded = pickle.load(open('imagesurl.p', 'rb'))
        creatingAnotherHit = True
        images = []
        for imm in os.listdir("images"):
            if "https://imagesformturk.s3.eu-central-1.amazonaws.com/" + imm not in uploaded:
                images.append(imm)
    except:
        creatingAnotherHit = False
        uploaded = []
        images = os.listdir("images")
    length = len(images)
    i = 0
    for img in images:
        if upload_to_aws("images/" + img, 'imagesformturk', img):
            i += 1
            uploaded.append("https://imagesformturk.s3.eu-central-1.amazonaws.com/" + img)
            percent = str(i * 100 / length)
            print (percent + '%')
    pickle.dump(uploaded, open('imagesurl.p', 'wb'))
    return creatingAnotherHit
