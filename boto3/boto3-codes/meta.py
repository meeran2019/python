
# List available region for ec2 service.
# Region is available in client object but not in resource object. 

# Import boto3 package. 
import boto3 

# Create the session for management console. 
aws_mag_con = boto3.session.Session()

# Create ec2 console. 
aws_ec2_con_res = aws_mag_con.resource(service_name='ec2')

# meta.client.operation()  -> Used to switch from resource to client. 
#print(dir(aws_ec2_con_res.meta.client.describe_regions))

#print(aws_ec2_con_res.meta.client.describe_regions()['Regions'])

for each in aws_ec2_con_res.meta.client.describe_regions()['Regions']:
    print(each['RegionName'])

