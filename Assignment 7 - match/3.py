"""Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit"""
print("-----------------------------------------------------------------------------------------------------------------------")
print("                                           Menu Driven                                                                 ")
print("a. Check whether a given set of three numbers are lengths of an isosceles triangle or no")
print("b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not")
print("c. Check whether a given set of three numbers are equilateral triangle or not")
print("Exit")
print("-------------------------------------------------------------------------------------------------------------------------")
choice = input("Enter  the choice a,b,c and d :")
match choice:
    case 'a':
        a = eval (input("Enter first length triangle of side :"))
        b = eval (input("Enter second length triangle of side :"))
        c = eval (input("Enter third length triangle of side :"))
        if a ==b or b==c or a==c:
            print("Isosceles triangle")
        else:
            print("Not,Isosceles triangle")
    case 'b' :
        a = eval (input("Enter first length triangle of side :"))
        b = eval (input("Enter second length triangle of side :"))
        c = eval (input("Enter third length triangle of side :"))
        if a != b or b == c or c !=  a :
            print("Right triangle ")
        else:
            print("Not,right triangle ")
    case 'c' :
        a = eval (input("Enter first length triangle of side :"))
        b = eval (input("Enter second length triangle of side :"))
        c = eval (input("Enter third length triangle of side :"))
        if a==b==c:
            print("Equilateral triangle")
        else:
            print("Not,Equilateral triangle")
    case 'd' :
        print("Exit")
        


