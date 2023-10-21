#list of dicts   ----> csv file
import csv
fields = ['eid','first_name','last_name']
dict_data = [
        # fields,
        {'eid':101,'first_name':'Shailesh','last_name':'Padalwar'},
        {'eid':102,'first_name':'santosh','last_name':'padala'},
        ] 
with open('emp2.csv','w') as f:
    writer = csv.DictWriter(f,fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict_data)
