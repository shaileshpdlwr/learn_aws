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