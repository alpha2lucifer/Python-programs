List = []
# Method for adding a new elements in List
def PushS(List):
    A = int(input("enter an element : "))
    List.append(A)
# method for deleting an element from the list
def PopS(List):
    if (List == []):
        print("stack empty !!")
    else :
        print("Deleted element : ",List.pop())

print(25*"#","|| List ||",25*"#")
print("push ☞ 1\npop ☞ 2\nexit ☞ 3")
while True :
    choice = int(input("enter choice : "))
    if (choice == 1):
        PushS(List)
    elif (choice == 2):
        PopS(List)
    elif (choice == 3):
        break
    else :
        print("enter a valid choice !!")
