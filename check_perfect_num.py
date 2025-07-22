def is_perfect(num: int) -> bool:
    sum = 1
    for i in range(2,num // 2 + 1):
        if num % i == 0:
            sum = sum + i
    return sum == num
def main():
    num = int(input("Enter an integer:"))
    if is_perfect(num):
        print("The number is perfect")
    else:
        print("The number is not perfect")
if __name__ == "__main__":
    main()
