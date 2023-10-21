#csv --> dicts
import csv 
with open('emp.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)