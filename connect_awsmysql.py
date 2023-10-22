import mysql.connector

mydb = mysql.connector.connect(
  database='csv_data',
  host="shailesh-mysql-aws.cbenh1xrfzji.ap-south-1.rds.amazonaws.com",
  user="shailesh",
  password="Padma#95"
)
mycursor = mydb.cursor()
insert_query = 'INSERT INTO employee(eid,enam,eaddr) values(%s,%s,%s);'
values = ('2','sai','Gunthur')
# print(insert_query)
mycursor.execute(insert_query,values)
mydb.commit()
print(mydb)