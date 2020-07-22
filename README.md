## Data analysis S3 and Ec2
This tool was created in Python3 to analyze informations of buckets in Amazon S3, showing about each bucket:
 - Name 
 - Date of creation
 - Number of files
 - Total size (KB)
 - Last modified date
 - Price

### Prerequisites 
Before you continue, please have met the following requirements:

* Create user in the IAM with permission AmazonS3FullAccess and configure the AWS credentials and region in your enviroment - see more in AWS documentation: [Configuration and credential file settings
](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
```
$ touch ~/.aws/credentials
```
```Credentials
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```
```Config
[default]
region = YOUR_PREFERRED_REGION
```
* Install the latest version of Python 3 and pip3
* Windows, Linux and Mac OS supported

### Install
In your terminal clone this repo:
```
git clone https://github.com/carolinebrasil/devops-challenge-ze.git

cd devops-challenge-ze
```
run the following command:
```
pip3 install -r requirements.txt
```

### How to use

```
$ python3 data-analysis-s3.py
```
or
```
$ python3 data-analysis-ec2.py
```

Expected output:
```
+----------------------+----------------------+----------------------+----------------------+----------------------+----------------------+
| Name                 | Creation date        |      Number of files |      Total size (KB) |  Last modified date  |                Price |
|----------------------+----------------------+----------------------+----------------------+----------------------+----------------------|
| challengeanalysis    | 2020-06-26           |                    5 |             1.662100 | 2020-06-26           |             0.000000 |
| challengeanalysis2   | 2019-09-20           |                    1 |             0.000000 | 2019-10-10           |             0.000000 |
| firstpythonbucket    | 2020-06-27           |                    2 |             0.683600 | 2020-06-28           |             0.000000 |
| secondpythonbucket   | 2020-06-27           |                    1 |             0.293000 | 2020-06-27           |             0.000000 |
```
