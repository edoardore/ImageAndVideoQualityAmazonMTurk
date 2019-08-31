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

hit_id_list =[]
images = pickle.load(open('imagesurl.p', 'rb'))
for img in images:
    response = client.create_hit_with_hit_type(
        HITLayoutId="39ZKK3W0VL0KX8EGGYE6VH1EX5H65S",
        HITTypeId="33JNTVT0Y4VGM52WIUOTF5W0G4N3WC",
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
    hit_id_list.append(hit_id)
pickle.dump(hit_id_list, open('hitid.p', 'wb'))
print("Your HIT has been created. You can see it at this link:")
print("https://workersandbox.mturk.com/mturk/preview?groupId=" + hit_type_id)
