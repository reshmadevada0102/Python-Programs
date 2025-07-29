def absolute(num):
    if num < 0:
        num = 0 - num
    return num

def power(num, power):
    result = 1
    for i in range(power):
        result = result * num
    return result

def factorial(num):
    result = 1
    for num in range(1,num + 1):
        result = result * num
    return result


