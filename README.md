# DLAMockProject
This Project is Django Rest Framework Project. In this project 3 endpoints are developed which will be used by DLA Mock Project Front end. 
- upload_data
- put_object
- list_objects

All of the above mentioned endpoints are accesible by giving access key in url parameter  

## upload_data endpoint
This is the POST API. In this end point you can insert data to S3 instance either by giving CSV data in request body or by uploading CSV file in form-data. 

### request Uploading file
`curl -i -H "Accept: application/json" -H "Content-Type: application/json" -F "path/to/the/file.csv" -X POST http://hostname/upload_data?access_key=JASHSDFAJKASKJF` 

### request uploading via request body
`curl -i -H "Accept: application/json" -H "Content-Type: application/json" -d {"dataType": "csv", "data":"sample,csv,data,in,comma,seperated,format", "dataSetName": "sampledataset"} -X POST http://hostname/upload_data?access_key=ASDASFDDCASD`
### response 
`{
    "dataUploaded": "Success",
    "ResponseMetadata": {
        "RequestId": "00000000000",
        "HostId": "sdfdsfsdfsdfsdf",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amz-id-2": "sampleknkfasfnsdknf",
            "x-amz-request-id": "00DFGD00SDF",
            "date": "Wed, 18 Mar 2020 12:22:26 GMT",
            "etag": "\"121739544ae9764eccd5e92088a06aeb\"",
            "content-length": "45236",
            "server": "AmazonS3"
        },
        "RetryAttempts": 1
    },
    "ETag": "\"121739544ae9764eccd5e92088a06aeb\""
}`


## List objects API
This is the GET API which is used to show the list of objects present in the S3 registry.

### request list 
`curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://hostname/list_objects?access_key=JASHSDFAJKASKJF`

### Sample Response 
`{
    "ResponseMetadata": {
        "RequestId": "CFD3E417DD0218FB",
        "HostId": "euILhg/ZtFZ56PvEgQ3f0ll8dEd0Tb6OSCcavmWaaIZE7ocSLgWCUB/8m505oWvtjfhw0ZLyhBk=",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amz-id-2": "euILhg/ZtFZ56PvEgQ3f0ll8dEd0Tb6OSCcavmWaaIZE7ocSLgWCUB/8m505oWvtjfhw0ZLyhBk=",
            "x-amz-request-id": "CFD3E417DD0218FB",
            "date": "Wed, 18 Mar 2020 12:20:59 GMT",
            "x-amz-bucket-region": "ap-southeast-1",
            "content-type": "application/xml",
            "transfer-encoding": "chunked",
            "server": "AmazonS3"
        },
        "RetryAttempts": 1
    },
    "IsTruncated": false,
    "Marker": "",
    "Contents": [
        {
            "Key": "FL_insurance_sample - Copy.csv",
            "LastModified": "2020-03-16T14:57:30Z",
            "ETag": "\"121739544ae9764eccd5e92088a06aeb\"",
            "Size": 4123652,
            "StorageClass": "STANDARD",
            "Owner": {
                "DisplayName": "aws.nbs38",
                "ID": "575a402e8810aac175ae785ae7153fb089ed12206b2c51c155188c5b89cdffa9"
            }
        },
        {
            "Key": "FL_insurance_sample.csv",
            "LastModified": "2020-03-16T14:44:04Z",
            "ETag": "\"d41d8cd98f00b204e9800998ecf8427e\"",
            "Size": 0,
            "StorageClass": "STANDARD",
            "Owner": {
                "DisplayName": "aws.nbs38",
                "ID": "575a402e8810aac175ae785ae7153fb089ed12206b2c51c155188c5b89cdffa9"
            }
        },
        {
            "Key": "FL_insurance_sampledasdasd.csv",
            "LastModified": "2020-03-16T14:58:57Z",
            "ETag": "\"121739544ae9764eccd5e92088a06aeb\"",
            "Size": 4123652,
            "StorageClass": "STANDARD",
            "Owner": {
                "DisplayName": "aws.nbs38",
                "ID": "575a402e8810aac175ae785ae7153fb089ed12206b2c51c155188c5b89cdffa9"
            }
        },
        {
            "Key": "test.csv",
            "LastModified": "2020-03-16T12:05:17Z",
            "ETag": "\"5a105e8b9d40e1329780d62ea2265d8a\"",
            "Size": 5,
            "StorageClass": "STANDARD",
            "Owner": {
                "DisplayName": "aws.nbs38",
                "ID": "575a402e8810aac175ae785ae7153fb089ed12206b2c51c155188c5b89cdffa9"
            }
        },
        {
            "Key": "testa.csv",
            "LastModified": "2020-03-16T12:50:17Z",
            "ETag": "\"ad0234829205b9033196ba818f7a872b\"",
            "Size": 5,
            "StorageClass": "STANDARD",
            "Owner": {
                "DisplayName": "aws.nbs38",
                "ID": "575a402e8810aac175ae785ae7153fb089ed12206b2c51c155188c5b89cdffa9"
            }
        }
    ],
    "Name": "dla-dsdsd-bucket",
    "Prefix": "",
    "MaxKeys": 1000,
    "EncodingType": "url"
}`

## Get Data endpoint
This is the GET API which is used to get the data from S3 registry. The data is fetched based on the Key. 

### request data 
`curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://hostname/list_objects?access_key=JASHSDFAJKASKJF&key=test.csv`

### sample response 
`{
    "ResponseMetadata": {
        "RequestId": "9C52069C222D1FA6",
        "HostId": "JKNBJKDFBJKbhkbkbhkJKBBJK=",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amz-id-2": "SDFSDFSDi/iIS7rLJuJsT9I2X2IqVER4EAmbegVFhQbow=",
            "x-amz-request-id": "9C52069C222D1FA6",
            "date": "Wed, 18 Mar 2020 12:33:32 GMT",
            "last-modified": "Mon, 16 Mar 2020 12:05:17 GMT",
            "etag": "\"5a105e8b9d40e1329780d62ea2265d8a\"",
            "x-amz-meta-format": "csv",
            "accept-ranges": "bytes",
            "content-type": "binary/octet-stream",
            "content-length": "5",
            "server": "AmazonS3"
        },
        "RetryAttempts": 1
    },
    "AcceptRanges": "bytes",
    "LastModified": "2020-03-16T12:05:17Z",
    "ContentLength": 5,
    "ETag": "\"5a105e8b9d40e1329780d62ea2265d8a\"",
    "ContentType": "binary/octet-stream",
    "Metadata": {
        "format": "csv"
    },
    "Body": [
        "test1"
    ]
}`
