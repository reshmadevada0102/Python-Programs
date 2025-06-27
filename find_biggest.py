def find_biggest(num1,num2):
    if num1>num2:
        print("The biggest number is:",num1)
    elif num2>num1:
        print("The biggest number is:",num2)
    else:
        print("Both are equal")
a=int(input("Enter first integer:"))
b=int(input("Enter second integer:"))
find_biggest(a,b)