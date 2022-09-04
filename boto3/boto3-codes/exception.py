import boto3 

try:
    import boto3
    print("Hello")
    mgm_con = boto3.session.Session(profile_name='dev')
except ModuleNotFoundError:
    print("Module not found error")
except Exception as e:
    print(e)
except boto3.exceptions.Boto3Error:
    print("Boto3 error")

#print(dir(boto3.exceptions))