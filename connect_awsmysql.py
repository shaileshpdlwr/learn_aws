import mysql.connector,os
from dotenv import load_dotenv
load_dotenv()
host = os.getenv('HOST')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')
mydb = mysql.connector.connect(
  database=database,
  host=host,
  user=user,
  password=password
)
mycursor = mydb.cursor()
insert_query = 'INSERT INTO employee(eid,enam,eaddr) values(%s,%s,%s);'
# values = ('2','sai','Gunthur')
# print(insert_query)
import csv
fields=['employee']
with open('emp2.csv',"r") as f:
    reader = csv.DictReader(f)
    for row in reader:
          values = (row['eid'],row['enam'],row['eaddr'])
          mycursor.execute(insert_query,values)
          print(row['eid'],row['enam'],row['eaddr'])
# mycursor.execute(insert_query,values)
mydb.commit()
# print(mydb)
