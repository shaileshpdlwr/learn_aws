import csv
#convert to csv file data
def create_csvdata(fields,data):
    with open('emp1.csv','w') as f:
        w = csv.writer(f)
        w.writerow(fields)
        w.writerows(data)

fields = ['eid','first_name','last_name','addr']
data = [
        # fields,
        ['101','Roshan','Naik','Yavatmal-MH'],
        ['102','Shailesh','Padalwar','Hyderabad-TS']
        ]


        
