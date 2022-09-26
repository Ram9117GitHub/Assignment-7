"""Write a python program to check whether a given string is a multiword string or single
word string using match case statement
"""
s = input("Enter a string :")
s.strip()
match s :
    case s if ' ' in s :
        print("Multiword")
    case s if ' '  not in s:
        print("Single word")
"""""""""""""""""""""""""""""""""""Output"""""""""""""""""""""""""""""""""""""""
"""
Enter a string :ramkumar
Single word
Enter a string :Ram kumar
Multiword
"""     