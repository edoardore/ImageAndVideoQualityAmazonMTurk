import boto3
import pickle
import imageManager

# Use the Amazon Mechanical Turk Sandbox to publish test Human Intelligence Tasks (HITs) without paying any money.
host = 'https://mturk-requester-sandbox.us-east-1.amazonaws.com'
# Uncomment line below to connect to the live marketplace instead of the sandbox
# host = 'https://mturk-requester.us-east-1.amazonaws.com'

region_name = 'us-east-1'
aws_access_key_id = 'AKIAR6AXQDP6P2MRTFFZ'
aws_secret_access_key = '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'
client = boto3.client('mturk',
                      endpoint_url=host,
                      region_name=region_name,
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      )
# Se si creano Hit aggiuntive mettere a True questa variabile
creatingAnotherHIT = imageManager.getImg()
if not creatingAnotherHIT:
    hit_id_list = []  # se prima volta inizializza la lista che colleziona le hit
    images = pickle.load(open('imagesurl.p', 'rb'))
else:
    hit_id_list = pickle.load(open('imageshitid.p',
                                   'rb'))  # se si vogliono aggiungere hit inizializzo anche con quelle create in precedenza per non perderle
    images = pickle.load(open('imagesurl.p', 'rb'))
    newImages = []
    oldImages = []
    for tuple in hit_id_list:
        oldImages.append(tuple[1])
    for img in images:
        if img not in oldImages:
            newImages.append(img)
    images = newImages
hit_type_id = None
for img in images:
    response = client.create_hit_with_hit_type(
        HITLayoutId="3TENGQN5S1KXRPUWS90R2E7L5KC21R",
        HITTypeId="3ZZSZV2CUBNO90XBT4LC1AIOEWXGSJ",
        HITLayoutParameters=[
            {
                'Name': 'img',
                'Value': img
            }, ],
        LifetimeInSeconds=600,  # Quanto resta disponibile una HIT a tutti i Workers, non il timer dopo aver accettato.
        MaxAssignments=5,
    )
    # The response included several fields that will be helpful later
    hit_type_id = response['HIT']['HITTypeId']
    hit_id = response['HIT']['HITId']
    tuple = []
    tuple.append(hit_id)
    tuple.append(img)
    hit_id_list.append(tuple)
    pickle.dump(hit_id_list, open('imageshitid.p', 'wb'))
if hit_type_id != None:
    print("Your HITs has been created at link:")
    print("https://workersandbox.mturk.com/mturk/preview?groupId=" + hit_type_id)
else:
    print 'Nothing added, the HITs is already pubblished'
