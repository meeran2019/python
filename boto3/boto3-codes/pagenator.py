
# import boto3 package. 
import boto3 

# create a aws management console session.
aws_mgm_con = boto3.session.Session()

# create ec2 console using client. 
aws_ec2_con = aws_mgm_con.client('ec2')

# create a paginator. 
paginator = aws_ec2_con.get_paginator('describe_instance_types')

# Paginate through the paginator using foor loop. 
# pagesize denotes the size of page.

for each_page in paginator.paginate(
    PaginationConfig={
        'PageSize': 30
    }
):
    print(len(each_page['InstanceTypes']))
    for each_value in each_page['InstanceTypes']:
        print(each_value['InstanceType'])

