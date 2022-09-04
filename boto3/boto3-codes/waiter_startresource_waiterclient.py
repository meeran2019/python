# In this example, start the instances using resource and CLient is used for waiter. 
# So can use both resource and waiter client. 

# import the boto3 package 
import boto3 

# open the aws management console 
aws_man_con = boto3.session.Session()

# open the ec2 console using resource and client. 
ec2_con_res = aws_man_con.resource('ec2')
ec2_con_cli = aws_man_con.client('ec2')

# Instance object used to pass the instance information. This is Resource. 
instance = ec2_con_res.Instance('i-029cb3d8ec1762624')
print("start the instance")
instance.start()

# Waiter is created using client object. 
print("waiter is used to check the status")
waiter = ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-029cb3d8ec1762624'])

print("Instance is running..")



