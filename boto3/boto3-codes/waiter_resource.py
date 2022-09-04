# import the boto3 package 
import boto3 

# open the aws management console 
aws_man_con = boto3.session.Session()

# open the ec2 console using resource. 
ec2_con_req = aws_man_con.resource('ec2')

# Instance object used to pass the instance information. 
instance = ec2_con_req.Instance('i-029cb3d8ec1762624')

# Instance object supports starts and other methods.
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance
# wait_until_running is used to wait till the instance is running. 
print("instance starts..")
instance.start()
instance.wait_until_running()
print("instance is running..")

# print(dir(instance))


