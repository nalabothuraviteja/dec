#!/usr/bin/env python
import os
import sys
import json
import boto3 

ec2client = boto3.client('ec2',region_name='us-east-2',aws_access_key_id='acces key id',aws_secret_access_key='secretkrey')



response = ec2client.describe_instances(
    Filters=[
        {
			'Name': 'tag:name',
            'Values': ['machine']
        }
    ]
    )
PublicIpAddress = ""
instancelist = []
for reservation in (response["Reservations"]):
    for instance in reservation["Instances"]:
       # host = host+"\'"+ PublicIpAddress + "\'"
        PublicIpAddress=instance["PublicIpAddress"]
        print "{\'group\': {\'hosts\': [\'"+PublicIpAddress+"\']}}"
