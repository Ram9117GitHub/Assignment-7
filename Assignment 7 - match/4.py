"""Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen."""
Age   = int(input("Enter Age number  :"))
match Age :
    case Age if Age<10:
        print("Kid")
    case Age if Age < 20:
            print("Teen")
    case Age if  Age < 40:
            print("Young")
    case Age if  Age < 60:
            print("Experienced")
    case Age if  Age >= 60:
            print("Senior Citizen")
    case _:
        print("Default number ")
""""""""""""""""""""""""""""Output"""""""""""""""""""""""""""""""""""
"""
Enter Age number  :9
Kid
Enter Age number  :56
Experienced
"""
