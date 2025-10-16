def square(n):
    if n > 0:
        print((n*n), end = " ")
        square(n - 1)
def main():
    n = int(input("Enter the value of n:"))
    square(n)
if __name__ == "__main__":
    main()