#importing csv
import csv

with open('Book1.csv', 'r') as F:
#other way to open file is f= ('storage\emulated\0\qpython\Book1.csv', 'r')
    reader = csv.reader(F)
# printing each line of the Data row by row 
    for row in reader:
        print(row)
    F.close()