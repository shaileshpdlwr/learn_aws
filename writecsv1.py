# List of lists ---> csv
import csv
fields = ['eid','first_name','last_name','addr']
data = [
        ['101','Roshan','Naik','Yavatmal-MH'],
        ['102','Shailesh','Padalwar','Hyderabad-TS']
        ]
with open('emp.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(data)