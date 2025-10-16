def sum_digit(num):
    sum = num
    while sum > 9:
        num = sum
        sum = 0
        while num > 0:
            sum = sum + num % 10
            num = num // 10
    return sum
def main():
    num = int(input("Enter the digit:"))
    result = sum_digit(num)
    print(result)
if __name__ == "__main__":
    main()