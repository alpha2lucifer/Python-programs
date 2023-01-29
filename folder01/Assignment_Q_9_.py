import csv 
with open('laps1.csv','w',newline='') as file :
    writer = csv.writer(file)
    writer.writerow(['ADMNO',"NAME","AGE"])
    writer.writerow([1151,"Ajay","12"])
    writer.writerow([1152,"Chandrika","14"])
print ("Record Added")