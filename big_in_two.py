def find_biggest(num1,num2):
    return num1 if num1 > num2 else num2
   

def main():
    #Take input from the user
    a=int (input("Enter first number:"))
    b=int (input("Enter second number:"))
    #call the function and pass inputs as arguments

    print(f"{find_biggest(a,b)} is big")

main()