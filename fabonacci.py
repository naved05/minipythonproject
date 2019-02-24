"""

Write a Python program to print the first 12 "even" Fibonacci numbers.

"""

def printFibonacciNumbers(n): 
      
    f1 = 1
    f2 = 1
    count=0
    if (n < 1): 
        return
    for x in range(0, n):
        if(f2%2==0 and count<=12):
            print(f2, end = " ")
            next = f1 + f2 
            f1 = f2 
            f2 = next
            count+=1
        else:
            next = f1 + f2 
            f1 = f2 
            f2 = next
          
# main code  
printFibonacciNumbers(30)
