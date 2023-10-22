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
