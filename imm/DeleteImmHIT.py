import boto3
from datetime import datetime
import pickle

# Get the MTurk client
mturk = boto3.client('mturk',
                     aws_access_key_id='AKIAR6AXQDP6P2MRTFFZ',
                     aws_secret_access_key='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',
                     region_name='us-east-1',
                     endpoint_url="https://mturk-requester-sandbox.us-east-1.amazonaws.com",
                     )

# Delete HITs
tuple = pickle.load(open('imageshitid.p', 'rb'))

for hit_id in tuple:
    print('HITId:', hit_id[0])

    # Get HIT status
    status = mturk.get_hit(HITId=hit_id[0])['HIT']['HITStatus']
    print('HITStatus:', status)

    # If HIT is active then set it to expire immediately
    if status == 'Assignable':
        response = mturk.update_expiration_for_hit(
            HITId=hit_id[0],
            ExpireAt=datetime(2015, 1, 1)
        )

        # Delete the HIT
    try:
        mturk.delete_hit(HITId=hit_id[0])
        hit_id[0].erease()
        hit_id[1].erease()
    except:
        print('Not deleted')
    else:
        print('Deleted')
    pickle.dump(tuple, open('imageshitid.p', 'wb'))
