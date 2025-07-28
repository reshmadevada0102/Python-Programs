def sum(num:int) -> int:
    if num < 10:
        return num
    else:
        return (num % 10) + sum(num // 10)
def main():
    num = int(input("Enter a number:"))
    print(f"The sum of digits of digits is {sum(num)}")
if __name__ == "__main__":
    main()
