# calculate the some basic calculations like addition,subtraction,multiply and divisions

def addition(x,y):
    return x+y
def substraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
def square(x,y):
    return x**y
def floordivision(x,y):
    return x//y

print("select operations :")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.divison")
print("5.square")
print("6.floordivision")


choice=input("enter your choice(1/2/3/4/5/6):")
n1=int(input("enter first number = "))
n2=int(input("enter second number = "))

if choice=="1":
 print(n1,"+",n2,"=",add(n1,n2))
elif choice=="2":
 print(n1,"-",n2,"=",subtraction(n1,n2))
elif choice=="3":
 print(n1,"*",n2,"=",multiplication(n1,n2))
elif choice=="4":
 print(n1,"/",n2,"=",division(n1,n2))
elif choice=="5":
 print(n2,"**",n2,"=",square(n1,n2))
elif choice=="6":
 print(n2,"//",n2,"=",floordivision(n1, n2))
else:
 print("sorry invalid input ..try to enter valid input and check.")

 