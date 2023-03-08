def add(a,b):
    print("Addition : ",a + b)
def subtract(a,b):
    print("Subtraction : ",a - b)
def multiply(a,b):
    print("Multiply : ",a * b)
def divide(a,b):
    print("Divide : ",a / b)
print("================================================")
print("=================Calculator=====================")
print("================================================")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice = input("Enter choice : ")
choice=int(choice)
num1 = input("Enter Number 1 : ")
num1=float(num1)
num2 = input("Enter Number 2 :")
num2=float(num2)
if(choice==1):
    add(num1,num2)
elif(choice==2):
    subtract(num1,num2)
elif(choice==3):
    multiply(num1,num2)
elif(choice==4):
    divide(num1,num2)


