a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))

if a==b==c:
    print("equilateral triangle")
elif a==b!=c or a!=b==c or a==c!=b:
    print("isosceles triangle")
else:
    print("scalane")