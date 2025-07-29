import checkpy as c
def main():
    input_num = int(input("Enter an integer"))
    if c.is_prime(input_num):
        print("Prime Number")
    else:
        print("Not a Prime Number")
    
if __name__ == "__main__":
    main()