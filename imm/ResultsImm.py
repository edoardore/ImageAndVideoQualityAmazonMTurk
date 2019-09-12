import boto3
import pickle
import xml.etree.ElementTree as ET
import pymysql
import Key

# Use the Amazon Mechanical Turk Sandbox to publish test Human Intelligence Tasks (HITs) without paying any money.
host = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
# Uncomment line below to connect to the live marketplace instead of the sandbox
# host = 'https://mturk-requester.us-east-1.amazonaws.com'

region_name = 'us-east-1'
aws_access_key_id = Key.getAws_access_key_id()
aws_secret_access_key = Key.getAws_secret_access_key()
client = boto3.client('mturk',
                      endpoint_url=host,
                      region_name=region_name,
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      )

# This HIT id should be the HIT you just created - see the CreateHITSample.py file for generating a HIT
hit_id_list = pickle.load(open('imageshitid.p', 'rb'))
for tuple in hit_id_list:
    hit_id = tuple[0]
    image = tuple[1][53:len(tuple[1])]
    hit = client.get_hit(HITId=hit_id)
    print ('Hit ' + hit_id + ' status: ' + hit['HIT']['HITStatus'])
    response = client.list_assignments_for_hit(
        HITId=hit_id,
        AssignmentStatuses=['Submitted'],
    )
    assignments = response['Assignments']
    numAssignmentSubmitted = len(assignments)
    print ('The number of submitted assignments is ' + str(numAssignmentSubmitted))
    MinAssignments = 3
    if numAssignmentSubmitted >= MinAssignments:
        for assignment in assignments:
            WorkerId = assignment['WorkerId']
            assignmentId = assignment['AssignmentId']
            answer = assignment['Answer']
            root = ET.fromstring(answer)
            nodes = root.findall(
                '{http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionFormAnswers.xsd}Answer')
            freetext = []
            for node in nodes:
                freetext.append(node.find(
                    '{http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionFormAnswers.xsd}FreeText').text)
            print (
                    'The Worker with ID ' + WorkerId + ' submitted assignment ' + assignmentId + ' and gave the answer: ')
            print freetext
            age = freetext[0]
            quality = freetext[1]
            resolution = freetext[2]
            db = pymysql.connect("localhost", "usertest", "123test", "dbmysql")
            # prepare a cursor object using cursor() method
            cursor = db.cursor()
            # Prepare SQL query to INSERT a record into the database.
            if (freetext[4] == 'true'):
                sex = 'M'
            else:
                sex = 'F'
            sqlSelect = "SELECT * FROM immquality WHERE WORKER_ID='%s' AND IMAGE_FILE='%s' AND QUALITY='%s' AND AGE='%s' AND SEX='%s' AND RESOLUTION='%s'" % (
                WorkerId, image, quality, age, sex, resolution)
            sqlInsert = "INSERT INTO immquality(WORKER_ID, IMAGE_FILE, QUALITY, AGE, SEX, RESOLUTION)VALUES" \
                        "('%s', '%s', '%s', '%s', '%s', '%s')" \
                        % (WorkerId, image, quality, age, sex, resolution)
            try:
                cursor.execute(sqlSelect)
                result = cursor.fetchall()
                # if the raw not in the table already
                if len(result) == 0:
                    # Execute the SQL command
                    cursor.execute(sqlInsert)
                    # Commit your changes in the database
                    db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()
            # disconnect from server
            db.close()
    else:
        print 'Waiting minimum another ' + str(3 - numAssignmentSubmitted) + ' assignments'
    print ''
