def is_prime(n: int) -> None:
    for i in range(2, n//2+1):
        if n%i == 0:
            print(f"{n} is Not a Prime Number")
            break
    else:
        print("Prime Number")

def main():
    x = int(input("Enter a number: "))
    is_prime(x)

if __name__ == "__main__":
    main()