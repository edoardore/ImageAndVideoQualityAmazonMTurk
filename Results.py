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

# This HIT id should be the HIT you just created - see the CreateHITSample.py file for generating a HIT
hit_id_list = pickle.load(open('hitid.p', 'rb'))
for hit_id in hit_id_list:
    hit = client.get_hit(HITId=hit_id)
    print ('Hit ' + hit_id + ' status: ' + hit['HIT']['HITStatus'])
    response = client.list_assignments_for_hit(
        HITId=hit_id,
        AssignmentStatuses=['Submitted'],
    )
    assignments = response['Assignments']
    print ('The number of submitted assignments is ' + str(len(assignments)))
    for assignment in assignments:
        WorkerId = assignment['WorkerId']
        assignmentId = assignment['AssignmentId']
        answer = assignment['Answer']
        print ('The Worker with ID ' + WorkerId + ' submitted assignment ' + assignmentId + ' and gave the answer: '
               + answer[answer.find('<FreeText>', 0) + 10:answer.find('</FreeText>', 0)])
    print ''