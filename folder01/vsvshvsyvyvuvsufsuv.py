import csv
f= open('attendees.csv')
csv_f=csv.reader()
for row in csv_f:
    print(row)