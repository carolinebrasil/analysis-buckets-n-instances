import boto3 # Lib to connect in AWS
from table_logger import TableLogger # Lib to exhibition data in table

ec2 = boto3.resource('ec2')

# Table to organize and show the information 
table = TableLogger(columns='ID, Name, Key, Type, Platform, State, Private_IP', border=False)

for i in ec2.instances.all():
    instancedata = dict() 
    instancedata['ID'] = i.id
    instancedata['Name'] = i.private_dns_name
    instancedata['Key'] = i.key_name
    instancedata['Type'] = i.instance_type
    instancedata['State'] = i.state['Name']
    instancedata['Private_IP'] = i.private_ip_address
    instancedata['Platform'] = i.platform

    # Show the information in table format
    table(instancedata['ID'], instancedata['Name'], instancedata['Key'], instancedata['Type'], instancedata['Platform'], instancedata['State'],instancedata['Private_IP'])
