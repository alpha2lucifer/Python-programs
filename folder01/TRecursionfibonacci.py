def Fibonacci_Recursion(n):  
   if n <= 1:  
       return n  
   else:  
       return(Fibonacci_Recursion(n-1) + Fibonacci_Recursion(n-2))  
nterms = int(input("Enter the terms? "))  # take input from the user
  
if nterms <= 0:  # check if the number is valid 
   print("Please enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(Fibonacci_Recursion(i))