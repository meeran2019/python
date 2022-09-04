# import boto3 package. 
import boto3

# It is login to AWS management console. 
my_session = boto3.session.Session(profile_name="default")

# dir() gives the list of objects available. 
print(dir(my_session))      

print(my_session.profile_name)

print(my_session.get_available_resources())

# IAM Console - Client 
iam_user_client = my_session.client("iam")

# IAM Console - Resource 
iam_user_resource = my_session.resource("iam")

# Get username using Client
print("Start using client..")
list_user = iam_user_client.list_users()

# It gives output in list. 
print(list_user['Users'])

# Since list, get the each value which gives output as dictionary. 
for each in list_user['Users']:
    print(each['UserName'])

print("End using client..")
print("Start using resources..")

list_user_resource = iam_user_resource.users.all()
print(list_user_resource)
for each in list_user_resource:
    print(each.name)

