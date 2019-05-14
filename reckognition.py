import boto3
import re

if __name__ == "__main__":

    bucket='bucket1io'
    photo='scan2.png'
    pattern='ZEA[0-9]+'
    client=boto3.client('rekognition')

  
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
                        
    textDetections=response['TextDetections']
    textDetections=str(textDetections)
    id=[]
    #for text in textDetections:
            # if re.search(pattern,text['DetectedText'].lower()):
            #     # print(type(text['DetectedText'].lower()))
            #     if text['DetectedText'] not in id:
            #         id.append(text['DetectedText'])
    
    val=re.findall(pattern,textDetections)
    val=set(val)
    print(val)
