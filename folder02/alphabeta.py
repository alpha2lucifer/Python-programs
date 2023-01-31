Package = []
# Method for adding a new package
def MakePush(Package):
    a = int(input ("enter package title : "))
    Package.append(a)
# method for deleting a package from the list
def MakePop(package):
    if (Package == []):
        print("stack empty !!")
    else :
        print("Deleted element : ",Package.pop())

print(25*"#","|| Package ||",25*"#")
print("push ☞ 1\npop ☞ 2\nexit ☞ 3")
while True :
    choice = int(input("enter choice : "))
    if (choice == 1):
        MakePush(Package)
    elif (choice == 2):
        MakePop(Package)
    elif (choice == 3):
        break
    else :
        print("enter a valid choice !!")

