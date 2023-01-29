import csv
filename = "numeral_csv_file.csv"
print("\n\n")
def AverageColumn(File):
    Data = []
    S = 0
    with open(File, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            Data.append(row)
    for i in Data :
        for e in i :
            S+=float(e)
        print(f"sum is : {S}",f" Average is : {S/len(e)}")
        S = 0
AverageColumn(filename)