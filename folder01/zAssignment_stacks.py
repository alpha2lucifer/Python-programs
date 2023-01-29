Book = []
# Method for adding a new Book
def Push(Book):
    book = input ("enter book name : ")
    Book.append(book)
# method for deleting a book from the list
def Pop(Book):
    if (Book == []):
        print("stack empty !!")
    else :
        print("Deleted book : ",Book.pop())
def Display(Book):
    if (Book == []):
        print("stack empty \nno book found !!")
    else :
        Top = len(Book)
        print(Book[Top-1])
        for x in range(Top-2,-1,-1):
            print(Book[x])
print(25*"#","|| Book ||",25*"#")
print("push ☞ 1\npop ☞ 2\ndisplay ☞ 3\nexit ☞ 4")
while True :
    choice = int(input("enter choice : "))
    if (choice == 1):
        Push(Book)
    elif (choice == 2):
        Pop(Book)
    elif (choice == 3):
        Display(Book)
    elif (choice == 4):
        break
    else :
        print("enter a valid choice !!")
