import boto3
import json
import glob
import errno

path='input/*.txt'
files=glob.glob(path)

client = boto3.client(service_name='comprehendmedical',region_name='us-east-1')

outfile=open('result.txt','a')

for name in files:
    with open(name) as f:
        text=f.read()
        result= client.detect_entities(Text=text)
        entities =result['Entities'];
        phi=client.detect_phi(
            Text=text
        )


        #---- Doctor Name and Patient Name ---#
        details=phi['Entities']
        dup_name=[]
        for data in details:
            
            if data['Type']=="NAME":
                dup_name.append(data['Text'])
        name=[]
        for x in dup_name:
            if x not in name:
                name.append(x)
        outfile.writelines(str("Patient Name: "+name[0]+"\n"))
        
        outfile.writelines(str("Doctor's Name: "+name[1]+"\n")) 
        # ------------------------------------#

        disease=[]
        for entity in entities:
            if entity['Category']=="MEDICAL_CONDITION" and len(entity['Traits'])!=0: #and entity['Text'].lower()=="diabetes" :
                if entity['Traits'][0]['Name'].lower()=="diagnosis":
                    disease.append(entity['Text'])
        disease=set(disease)
        outfile.writelines(str("Problems : "+disease+"\n"))

        # for entity in entities:
        #     if entity['Category']=="MEDICAL_CONDITION" and len(entity['Traits'])!=0:
        #         if entity['Traits'][0]['Name'].lower()=="diagnosis":
outfile.close()
     