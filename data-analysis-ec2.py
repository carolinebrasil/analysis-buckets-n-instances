import boto3 # Lib to connect in AWS
from table_logger import TableLogger # Lib to exhibition data in table

ec2 = boto3.resource('ec2')

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

    # Show the information in table format
    table(instancedata['Creation_date'],instancedata['ID'], instancedata['Type'], instancedata['State'],instancedata['Public_IP'])
