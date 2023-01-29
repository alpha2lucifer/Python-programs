import csv as C
print("\n")
with open("Test_csv_file.csv","r") as F :
    A = C.reader(F)
    file_data = list(A)
for list in file_data :
    for element in list :
        print("\t|",element,end = "")
    print()
    