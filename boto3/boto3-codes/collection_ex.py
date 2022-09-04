
import boto3 

aws_mgm_con = boto3.session.Session()

aws_ec2_con = aws_mgm_con.resource('ec2')

instances = aws_ec2_con.instances.all()

for each in instances:
    print(each.id)
