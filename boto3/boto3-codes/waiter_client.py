# import the boto3 package 
import boto3 

# open the aws management console 
aws_man_con = boto3.session.Session()

# open the ec2 console. 
ec2_con_cli = aws_man_con.client('ec2')

# start the instance 
# NOTE: Once start_instance triggered, it move to next statement. Wont check whether it is in running status.
print ("Start the instances..")
response = ec2_con_cli.start_instances(InstanceIds = ['i-029cb3d8ec1762624'])

# Waiter is used to wait to check whether instance running. 
waiter = ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-029cb3d8ec1762624'])
print("Instance is running ... ")

# get the instance id. 
response = ec2_con_cli.describe_instances(InstanceIds=['i-029cb3d8ec1762624'])
for each in response['Reservations']:
    for each_instance in each['Instances']:
        print(each_instance['InstanceId'])

