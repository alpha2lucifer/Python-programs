import csv
csv.register_dialect('myDialect',delimiter = ',',quoting=csv.QUOTE_ALL,skipinitialspace=True) 
f=open('Book1.csv','r')
reader = csv.reader(f, dialect='myDialect')
for row in reader:
    print(row)