'''WAP to check whether a number is prime or not using two different functions'''
def check_prime(num):
    for i in range(2, (num//2) + 1):
        if num % i == 0:
            return False 
    else:
        return True
    
def main():
    num = int(input("Enter an integer:"))

    if check_prime(num) == True:
        print(f"The {num} is prime number")
    else:
        print(f'The {num} is not a prime number')
if __name__ == "__main__":
    main()