import os
import io
import boto3
import json
import csv
from io import StringIO

# grab static variables
sagemaker = boto3.client('sagemaker')
ENDPOINT_NAME = 'demobb-invoice-prediction'
runtime= boto3.client('runtime.sagemaker')



def lambda_handler(event, context):
    
    # TEST THE ENDPOINT WITH A SAMPLE
    line = '5,4.60,1,26.16,1,1.0,21.0,0.2076,2,7,21,2,7,49,4.6750,0.9840,1,0,1'
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                           ContentType='text/csv',
                                           Body=line)
    result = json.loads(response['Body'].read().decode())

    return result
