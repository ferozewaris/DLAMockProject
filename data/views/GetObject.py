from rest_framework.views import APIView
import boto3
from rest_framework import status
from rest_framework.response import Response
import os

BUCKET_NAME = 'dla-test-bucket'
SECRET_KEY = os.environ['SECRET_KEY']

class GetObjectView(APIView):
    def get(self, request):
        ACCESS_KEY = request.GET['access_key']
        S3Clinet = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
        responseCode = status.HTTP_200_OK
        restResponse = {}
        key = request.GET['key']
        objectResponse = S3Clinet.get_object(Bucket=BUCKET_NAME, Key=key)
        if objectResponse['ResponseMetadata']['HTTPStatusCode'] == 200:
            restResponse.update(objectResponse)
        else:
            restResponse.update({'GetObjectRequest': 'failed'})
            responseCode = status.HTTP_400_BAD_REQUEST
        return Response(data=restResponse, status=responseCode)