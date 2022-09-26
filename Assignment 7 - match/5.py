"""
Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.
"""
num  = int(input("Enter the number  :"))
match num :
    case num if num%2==0:
        print("Saurabh Shukla")
    case num if num <0 and num%2 :
        print("Prateek Jain") 
    case num if num>0  and   num %2:
        print("Aditya Choudhary")
"""""""""""""""""""""""Output"""""""""""""""""""""""""""
"""
Enter the number  :4
Saurabh Shukla
Enter the number  :3
Aditya Choudhary
Enter the number  :-3
Prateek Jain
"""

    

