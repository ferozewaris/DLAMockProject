from django.shortcuts import render
import boto3
from rest_framework.decorators import api_view, authentication_classes, permission_classes
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
import os

BUCKET_NAME = 'XXXXXXXXX'
SECRET_KEY = os.environ['SECRET_KEY']
# Create your views here.


@api_view(['POST'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def upload_data(request):
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
        key = str(dataSetName)+'.csv'
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


@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def list_objects(request):
    ACCESS_KEY = request.GET['access_key']
    S3Clinet = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    responseCode = status.HTTP_200_OK
    restResponse = {}
    list_response = S3Clinet.list_objects(Bucket=BUCKET_NAME)
    if list_response['ResponseMetadata']['HTTPStatusCode'] == 200:
        restResponse.update(list_response)
    else:
        restResponse.update({'GetListRequest': 'failed'})
        responseCode=status.HTTP_400_BAD_REQUEST
    return Response(data=restResponse, status=responseCode)

@api_view(['GET'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def get_object(request):
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

