import csv
F = open("students.csv","w")
A = csv.writer(F)
A.writerow(["Admno","StudenName","City","Remarks"])
F.close()
1