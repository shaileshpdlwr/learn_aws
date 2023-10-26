#Aws Task 1 :
Dump data from csv file to s3 bucket and return data using lambda function .
==> 
  1. Create S3 Bucket
  2. Create IAM Role : S3 full access,cloudwatch full access
  3. create lambda function which should trigger when S3 uploads .
  4. Add trigger as 3rd point
  # At lambda function
  s3_bucket_name=event['Records']record[0]['s3']['bucket']['name']
  uploaded_object_path=event['Records']record[0]['s3']['object']['key']

#22-Octo-2023
=============
aws-mysql and local python connection and some operations .  


# How to dump s3 to aws - mySql ?
```bash
import json
import csv
import boto3
import mysql.connector

s3client=boto3.client('s3')
def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    csv_file = event['Records'][0]['s3']['object']['key']
    response = s3client.get_object(Bucket=bucket, Key=csv_file)
    lines = response['Body'].read().decode('utf-8').split()
    results = []
    for row in csv.DictReader(lines):
        results.append(row.values())
    print(results)
    
    connection = mysql.connector.connect(host='mysql.c79sd2kyheg7.us-east-1.rds.amazonaws.com',
                                         database='employeedb',
                                         port='3306',
                                         user='admin',
                                         passwd='admin123')
    
    mysql_insert = "insert into employee(empid,ename,salary) values(%s,%s,%s)"
    
    cursor = connection.cursor()
    cursor.executemany(mysql_insert, results)
    connection.commit()
```
# AWS - API GATEWAY
# Que1 : What is Amazon API Gateway?
Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor and secure APIs at any scale. 
# git tags
1. What are tags / releases
2. Why should i create TAGs
3. When to create TAGs
4. How to create TAGs in git
     create | show | publish | delete

Step 1:
Checkout the branch where you want to create the tag
```git checkout "branch name"``
example : ```git checkout master```
________________________________________________________

Step 2:
Create tag with some name
```bash
git tag "tag name"
```
example : git tag v1.0
git tag -a v1.0 -m "ver 1 of .."  (to create annotated tags) 
________________________________________________________

Step 3:
Display or Show tags
git tag
git show v1.0
git tag -l “v1.*”
________________________________________________________

Step 4:
Push tags to remote
git push origin v1.0
git push origin --tags
git push --tags 
(to push all tags at once)
________________________________________________________

Step 5:
Delete tags (if required only)
to delete tags from local :
git tag -d v1.0
git tag --delete v1.0

to delete tags from remote :
git push origin -d v1.0
git push origin --delete v1.0
git push origin :v1.0

to delete multiple tags at once:
git tag -d v1.0 v1.1 (local)
git push origin -d v1.0 v1.1 (remote)

________________________________________________________


Checking out TAGS

We cannot checkout tags in git
We can create a branch from a tag and checkout the branch
git checkout -b "branch name" "tag name"
example : git checkout -b ReleaseVer1 v1.0
________________________________________________________

Creating TAGS from past commits

git tag "tag name" "reference of commit"
example : git tag  v1.2 5fcdb03

 