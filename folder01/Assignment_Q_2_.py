import csv
L = [["alpha",13,23], ["beta",7,18], ["gamma",2,9], ["delta",34,17], ["Charlie",24,67]]
with open("CSVfile.csv", "w", newline="") as F :
   W= csv.writer(F)
   W.writerows(L)
with open('CSVfile.csv', newline="") as csvfile:
 L = csv.reader(csvfile, delimiter=' ')
 for D in L:
   print(', '.join(D))
