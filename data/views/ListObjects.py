from rest_framework.views import APIView
import boto3
from rest_framework import status
from rest_framework.response import Response
import os

BUCKET_NAME = 'dla-test-bucket'
SECRET_KEY = os.environ['SECRET_KEY']

class ListObjectsView(APIView):
    def get(self, request):
        print("in list object get function")
        ACCESS_KEY = request.GET['access_key']
        S3Clinet = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
        responseCode = status.HTTP_200_OK
        restResponse = {}
        list_response = S3Clinet.list_objects(Bucket=BUCKET_NAME)
        if list_response['ResponseMetadata']['HTTPStatusCode'] == 200:
            restResponse.update(list_response)
        else:
            restResponse.update({'GetListRequest': 'failed'})
            responseCode = status.HTTP_400_BAD_REQUEST
        return Response(data=restResponse, status=responseCode)
