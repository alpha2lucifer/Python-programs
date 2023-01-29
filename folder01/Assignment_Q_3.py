import csv
with open('CSV_file.csv',mode = 'a') as csvfile:
    W = csv.writer(csvfile, delimiter = ',')
    choice = 'y'
    while "y" in choice.lower() :
        employee_number = int(input("\nenter employee Number : "))
        employee_name = input("enter employee Name   : ")
        employee_salary = int(input("enter employee Salary : "))
        W.writerow([employee_number, employee_name, employee_salary])
        print(10*"#","Data appended",10*"#")
        choice = input("Do you want to add more data ? \n\t")