""" Write a python program to check whether a given number is positive, negative or zero using match case statement
"""
num = int(input("Enter a number :"))
match num :
    case num if  num >0:
        print("Positive number ")
    case num if  num<0:
        print("Negative number")
    case num if  num ==0:
        print("Zaro number")
"""""""""""""""""""""""""""""""""Output"""""""""""""""""""""""""""""
"""
Enter a number :6
Positive number 
Enter a number :-7
Negative number
Enter a number :0
Zaro number

"""