from rest_framework.views import APIView
import boto3
from rest_framework import status
from rest_framework.response import Response
import os

BUCKET_NAME = 'dla-test-bucket'
SECRET_KEY = os.environ['SECRET_KEY']

class UploadDataView(APIView):
    def post(self, request):
        ACCESS_KEY = request.GET['access_key']
        S3Clinet = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
        responseCode = status.HTTP_200_OK
        restResponse = {}
        body = request.body
        try:
            file = request.FILES['file']
            print("in try")
            # file.read()
            content = file.read()
            filename = file.__str__()
            if filename[-4:] == '.csv':
                uploadResponse = S3Clinet.put_object(Body=content, Bucket=BUCKET_NAME, Key=filename,
                                                     Metadata={'format': filename[-4:]
                                                               })
                if uploadResponse['ResponseMetadata']['HTTPStatusCode'] == 200:
                    restResponse.update({'dataUploaded': 'Success'})
                    restResponse.update(uploadResponse)
                else:
                    restResponse.update({'dataUploaded': 'failed'})
                    restResponse.update(uploadResponse)
                    responseCode = status.HTTP_400_BAD_REQUEST

        except:

            dataType = body['type']
            data = body['data']
            dataSetName = body['dataSetName']
            key = str(dataSetName) + '.csv'
            uploadResponse = S3Clinet.put_object(Body=data.encode(), Bucket=BUCKET_NAME, Key=key,
                                                 Metadata={
                                                     'format': dataType
                                                 }
                                                 )
            if uploadResponse['ResponseMetadata']['HTTPStatusCode'] == 200:
                restResponse.update({'dataUploaded': 'Success'})
                restResponse.update(uploadResponse)
            else:
                restResponse.update({'dataUploaded': 'failed'})
                restResponse.update(uploadResponse)
                responseCode = status.HTTP_400_BAD_REQUEST

        return Response(data=restResponse, status=responseCode)