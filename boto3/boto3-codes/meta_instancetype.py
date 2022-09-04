# import boto3 package.
import boto3 

# create a session.
aws_mgm_con = boto3.session.Session()

# create a ec2 console using resource. 
ec2_con_res = aws_mgm_con.resource('ec2')

#print(ec2_con_res.meta.client.describe_instance_types()['InstanceTypes'])

# using meta.client to switch to client object. 
for each in ec2_con_res.meta.client.describe_instance_types()['InstanceTypes']:
    print(each['InstanceType'])
