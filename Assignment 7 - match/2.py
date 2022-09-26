"""Write a menu driven program to perform following operations - Addition, Subtraction,Multiplication, Division"""
print("----------------------------------------------------------------------------------------------------------")
print("                                  Menu Driven                                        ")
print("1. Addition ")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("--------------------------------------------------------------------------------------------------------------")
num = int(input("Enter the choice number 1,2,3,4 :"))
match num :
    case 1:
        num1 = int(input("Enetr a first number :"))
        num2 = int(input("Enter second number :"))
        Adition = num1 +num2
        print(Adition) 
    case 2:
        num1 = int(input("Enetr a first number :"))
        num2 = int(input("Enter second number :"))
        Sub  = num1 +num2
        print(Sub)
    case 3:
        num1 = int(input("Enetr a first number :"))
        num2 = int(input("Enter second number :"))
        Multi = num1 +num2
        print(Multi) 
    case 4:
        num1 = int(input("Enetr a first number :"))
        num2 = int(input("Enter second number :"))
        Div = num1 +num2
        print(Div)  
""""""""""""""""""""""""""""""""""""""""""""""""""""Output"""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
Enter the choice number 1,2,3,4 :1
Enetr a first number :23
Enter second number :4
27
"""
