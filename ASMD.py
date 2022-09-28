# simple python program to mathematics operations

import math

def add(a, b):
    return(a + b) #this functions add's two numbers

def sub(a, b) :
    return(a - b)

def mul(a, b):
    return(a * b)

def div(a, b) :
    return(a * b)

def greater(a, b) :
    if a > b :
        print(a, "is grater than b")
    else:
        print(b, "is greater than a")

def factorial(a) :
    return 1 if (a == 0) or (a == 1) else a * factorial(a-1)

def IsPerfectSquare(a):
    s = int(math.sqrt(a))
    return s*s == a

def IsFibionci(b):
    return IsPerfectSquare(5*b*b + 5) or IsPerfectSquare(5*b*b -4)

def SumOfSeries(a) :
    sum = 0
    return sum

########################################################
print("Select the operation you want to perform")      #
print("1. Addition")                                   #
print("2. Subtraction")                                #
print("3. Multiplication")                             #
print("4. Division")                                   #
print("5. Greater than or less than")                  #
print("6. Factorial")                                  #
print("7. Range of fibionci numbers")                  #
########################################################


while True :
    choice = input("Enter a mode : ")

    if choice in ('1','2','3','4','5','6','7','8'):
        num1 = int(input("Enter a number : "))
        num2 = int(input("Enter a number : "))


        if choice == '1' :
            print("The addition of given 2 numbers are :", add(num1, num2))

        elif choice == '2' :
            print("The subtraction of given 2 numbers are :", sub(num1, num2))

        elif choice == '3' :
            print("The multiplication of given 2 numbers are :", mul(num1, num2))

        elif choice == '4' :
            print("The division of given 2 numbers are : ", div(num1, num2))

        elif choice == '5' :
            print("The greatest number is :", greater(num1, num2))

        elif choice == '6' :
            print("The factorial of number is (Type the same number 2 times) :" , factorial(num1))
        
        elif choice == '7' :
            for i in range(num1, num2) :
                if (IsFibionci(i)== True) :
                    print(i, "is a fibionci number")
                else :
                    print(i, "is not a fibionci number")
        elif choice == '8' :
            for i in range(num1):
                sum +=i*i*i
                

            print("(NOTE : type num1 and num2 as same) The sum of n cube numbers are ", SumOfSeries(num1))


        next_calculation = input("Enter a choice (yes/no) : ")
        if next_calculation == "no" :
            break

    else :
        print("Invalid Input") 
