import csv
with open(“testfile.csv”) as f :
#1
    r= csv.reader(f)
#2
    for row in r:
#3
        print(row)#4