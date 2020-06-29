import boto3 # Lib for collect information in AWS s3
from table_logger import TableLogger # Lib to exhibition data in table

'''
Stage to collect information for each bucket in AWS S3.
Name, date of creation, number of files, total size in KB, last modified date of the most recent file and cost.
'''
# Resource s3
s3 = boto3.resource('s3') 

# Table to organize and show the information 
table = TableLogger(columns='Name,Creation date,Number of files,Total size (KB),Last modified date,Price', border=True)

# tax for s3 in us-east-1
tax = 0.023  

for s3_bucket in (s3.buckets.all()):
    # Dictionary to store bucket informations 
    bucketdata = dict() 
    
    # Bucket name
    bucketdata['name'] = s3_bucket.name

    # Date of creation
    bucketdata['creation_date'] = s3_bucket.creation_date.strftime("%Y-%m-%d")

    # Number of files 
    bucketdata['number_files'] = int(sum(1 for count in s3_bucket.objects.all()))
    
    # Total bucket size with conversion Byte to KB
    bucketdata['total_size_KB'] = round(float(sum(o.size for o in s3_bucket.objects.all())) / 1024, 4)
    
    # Last modified date of most recent file 
    bucketdata['last_modified'] = max(s3_bucket.objects.all(), key=lambda o: o.last_modified, default=None)
    if bucketdata['last_modified'] is None:
        bucketdata['last_modified'] = bucketdata['creation_date'].creation_date.strftime("%Y-%m-%d")
    else:
        bucketdata['last_modified'] = bucketdata['last_modified'].last_modified.strftime("%Y-%m-%d")
    
    # Calculate price with tax standard for us-east-1 in GB
    bucketdata['pricing'] = round(bucketdata['total_size_KB'] / 1024**2 * tax, 4)

    # # Show the information in table format
    table(bucketdata['name'], bucketdata['creation_date'], bucketdata['number_files'], bucketdata['total_size_KB'], bucketdata['last_modified'], bucketdata['pricing'])
