import boto3
import pickle

# Use the Amazon Mechanical Turk Sandbox to publish test Human Intelligence Tasks (HITs) without paying any money.
host = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
# Uncomment line below to connect to the live marketplace instead of the sandbox
# host = 'https://mturk-requester.us-east-1.amazonaws.com'

region_name = 'us-east-1'
aws_access_key_id = ''
aws_secret_access_key = ''
client = boto3.client('mturk',
                      endpoint_url=host,
                      region_name=region_name,
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      )

hit_id_list = []
images = pickle.load(open('imagesurl.p', 'rb'))
for img in images:
    response = client.create_hit_with_hit_type(
        HITLayoutId="3TENGQN5S1KXRPUWS90R2E7L5KC21R",
        HITTypeId="3ZZSZV2CUBNO90XBT4LC1AIOEWXGSJ",
        HITLayoutParameters=[
            {
                'Name': 'img',
                'Value': img
            }, ],
        LifetimeInSeconds=60,
        MaxAssignments=5,
    )
    # The response included several fields that will be helpful later
    hit_type_id = response['HIT']['HITTypeId']
    hit_id = response['HIT']['HITId']
    tuple = []
    tuple.append(hit_id)
    tuple.append(img)
    hit_id_list.append(tuple)
pickle.dump(hit_id_list, open('hitid.p', 'wb'))
print("Your HITs has been created at link:")
print("https://workersandbox.mturk.com/mturk/preview?groupId=" + hit_type_id)
