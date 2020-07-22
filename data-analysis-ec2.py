import boto3 # Lib to connect in AWS
from table_logger import TableLogger # Lib to exhibition data in table

ec2 = boto3.resource('ec2')
    #   aws_access_key_id= 'AKIAY2SAYD6DBURO54VD',
    #   aws_secret_access_key= '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%',
    #   region_name = 'us-east-1')

# Table to organize and show the information 
table = TableLogger(columns='Creation date, ID, Type,State, Private_IP', border=True)

for i in ec2.instances.all():
    instancedata = dict() 
    instancedata['ID'] = i.id
    instancedata['Type'] = i.instance_type
    instancedata['State'] = i.state['Name']
    instancedata['Public_IP'] = i.private_ip_address
    instancedata['Creation_date'] = i.launch_time
    #instancedata['security_groups'] = i.security_groups
    #print(i)
    # Show the information in table format
    table(instancedata['Creation_date'],instancedata['ID'], instancedata['Type'], instancedata['State'],instancedata['Public_IP'])