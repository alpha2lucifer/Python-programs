import csv
Data = []
response = 'y'
while 'y' in response.lower() :
    code = input("\nEnter item code :")
    name = input("Enter name :")
    price = input("Enter price :")
    qty = input("Enter Quantity :")
    Data.append([ code, name, price, qty ])
    response = input("Do you want to add more data ? \n\t")
        
with open("Groceries.csv","w",newline="") as f :
    w = csv.writer(f,delimiter=',')
    w.writerows(Data)