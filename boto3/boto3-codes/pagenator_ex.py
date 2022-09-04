import boto3 

aws_mgm_con = boto3.session.Session()
aws_ec2_con = aws_mgm_con.client('ec2')

paginator = aws_ec2_con.get_paginator('describe_instances')
for each_page in paginator.paginate(
    PaginationConfig={
        'PageSize': 5}
):
    for each_instance in each_page['Reservations']:
        for each_instances in each_instance['Instances']:
            print(each_instances['InstanceId'])

