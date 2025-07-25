def is_strong(num: int) -> bool:
    temp = num
    sum = 0
    while temp > 0:
        sum = sum + fact(temp % 10)
        temp = temp // 10
    return sum == num

def fact(num: int) -> int:
    res = 1
    for i in range(2, num + 1):
        res *= i
    return res

def main():
    num= int(input('Enter an integer:'))
    if is_strong(num):
        print(f'{num} is a strong number')
    else:
        print(f'{num} is not a strong number')
if __name__ == "__main__":
    main()