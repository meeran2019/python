# import boto3 package. 
import boto3

# create the aws management console session. 
aws_man_con = boto3.session.Session()

# create STS client object. 
sts_client = aws_man_con.client('sts')

# call the caller identity object. 
response = sts_client.get_caller_identity()
print(response['Account'])

# get session token credentials.
response = sts_client.get_session_token()
print(response)
print(response['Credentials']['AccessKeyId'])
print(response['Credentials']['SecretAccessKey'])

