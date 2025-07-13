def all_prime() -> None:
    count = 0
    for n in range(2, 1001):
        for i in range(2, n//2+1):
            if n%i == 0:
                break
        else:
            print(n, end=' ')
            count = count + 1
    print(f"\n There are {count} Prime Numbers")
    print("There are", count, "prime number")


def main():
    
    all_prime()

if __name__ == "__main__":
    main()