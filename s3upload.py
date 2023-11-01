import boto3

s3_client = boto3.client('s3')
# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)
bucket_name = 'django-app-blog'
file_key = 's3folder/emp.csv'
local_file_path = '/home/shailesh/Desktop/shaileshL/aws/learn_aws/emp.csv'
# Upload the file to S3
s3_client.upload_file(local_file_path, bucket_name, file_key)
print(f'File uploaded to S3 bucket {bucket_name} with key {file_key}')
