import boto3
from botocore.exceptions import NoCredentialsError
import os
import pickle
import mimetypes
import Key


def getVideo():
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
        uploaded = pickle.load(open('videosurl.p', 'rb'))
        creatingAnotherHit = True
        videos = []
        for vid in os.listdir("videos"):
            if "https://videosformturk.s3.eu-central-1.amazonaws.com/" + vid not in uploaded:
                videos.append(vid)
    except:
        creatingAnotherHit = False
        uploaded = []
        videos = os.listdir("videos")
    length = len(videos)
    i = 0
    for vid in videos:
        if upload_to_aws("videos/" + vid, 'videosformturk', vid):
            i += 1
            uploaded.append("https://videosformturk.s3.eu-central-1.amazonaws.com/" + vid)
            percent = str(i * 100 / length)
            print (percent + '%')
    pickle.dump(uploaded, open('videosurl.p', 'wb'))
    return creatingAnotherHit
