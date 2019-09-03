import boto3
from datetime import datetime
import pickle

# Get the MTurk client
mturk = boto3.client('mturk',
                     aws_access_key_id='',
                     aws_secret_access_key='',
                     region_name='us-east-1',
                     endpoint_url="https://mturk-requester-sandbox.us-east-1.amazonaws.com",
                     )

# Delete HITs
tuple = pickle.load(open('hitid.p', 'rb'))

for hit_id in tuple:
    print('HITId:', hit_id[0])

    # Get HIT status
    status = mturk.get_hit(HITId=hit_id[0])['HIT']['HITStatus']
    print('HITStatus:', status)

    # If HIT is active then set it to expire immediately
    if status == 'Assignable':
        response = mturk.update_expiration_for_hit(
            HITId=hit_id,
            ExpireAt=datetime(2015, 1, 1)
        )

        # Delete the HIT
    try:
        mturk.delete_hit(HITId=hit_id[0])
    except:
        print('Not deleted')
    else:
        print('Deleted')
