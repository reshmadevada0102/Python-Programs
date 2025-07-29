def is_prime(num: int) -> bool:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num: int)  -> bool:
    rev = 0
    temp = num
    while temp > 0:
        rev = (rev * 10) + (temp % 10)
        temp = temp // 10
    return num == rev

def is_perfect(num: int) -> bool:
    sum = 1
    for i in range(2,num // 2 + 1):
        if num % i == 0:
            sum = sum + i
    return sum == num

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

def is_armstrong(num: int) -> bool:
    temp = num
    sum = 0
    while temp > 0:
        sum = sum + (temp % 10) ** 3
    return sum == num
