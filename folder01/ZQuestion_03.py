Student = []
# Method for adding a new Student
def Push(Student):
    name = input ("enter Student name : ")
    ID = int(input("enter Student id : "))
    Student.append([name,ID])
# method for deleting a Student data from the list
def Pop(Student):
    if (Student == []):
        print("stack empty !!")
    else :
        print("Deleted Student : ",Student.pop())
print(25*"#","|| Students ||",25*"#")
print("push ☞1\npop ☞ 2\nexit ☞3")
while True :
    choice = int(input("enter choice : "))
    if (choice == 1):
        Push(Student)
    elif (choice == 2):
        Pop(Student)
    elif (choice == 3):
        break
    else :
        print("enter a valid choice !!")
