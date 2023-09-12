import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_state = instance['State']['Name']
        instance_type = instance['InstanceType']
        instance_launch_time = instance['LaunchTime']

        print(f"Instance ID: {instance_id}")
        print(f"State: {instance_state}")
        print(f"Instance Type: {instance_type}")
        print(f"Launch Time: {instance_launch_time}")
        print("\n")
