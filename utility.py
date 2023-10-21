import csv
#convert to csv file data
def create_csvdata(fields,data):
    #list of lists ---> csv file
    with open('emp.csv','w') as f:
        w = csv.writer(f)
        w.writerow(fields)
        w.writerows(data)

    #list of dicts ---> csv file
    with open('emp1.csv',w) as f1:
        list_dict = data
        w1 = csv.DictWriter(f1,fieldnames=fields)
        w1.writeheader()
        w1.writerows(list_dict)

fields = ['eid','first_name','last_name','addr']
data = [
        # fields,
        ['101','Roshan','Naik','Yavatmal-MH'],
        ['102','Shailesh','Padalwar','Hyderabad-TS']
        ]

# create_csvdata(fields,data)

def create_csvFromDict(fields,dict_data):
    with open("emp_dict.csv",'w',newline='') as f:
        w = csv.DictWriter(f,fieldnames=fields)
        # w.writerow(fields)
        w.writeheader()
        w.writerows(dict_data)
fields = ['eid','first_name','last_name']
dict_data = [
        # fields,
        {'eid':101,'first_name':'Shailesh','last_name':'Padalwar'},
        {'eid':102,'first_name':'santosh','last_name':'padala'},
        ]  
      
create_csvFromDict(fields=fields,dict_data=dict_data)