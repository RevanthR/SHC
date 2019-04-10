import boto3
import json

f=open("data.txt","r")
client = boto3.client(service_name='comprehendmedical',region_name='us-east-1')
text=f.read()
result= client.detect_entities(Text=text)
entities =result['Entities'][0]['Category'];
phi=client.detect_phi(
    Text=text
)

# for entity in entities:
#     print(entity,'\n\n')

print(entities)
# print(phi)