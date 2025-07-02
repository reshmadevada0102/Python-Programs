def fun() -> None:
    num = int(input("Enter an integer"))
    sum = 0
    prod = 1
    while num > 0:
        sum = sum + num % 10
        prod = prod * num % 10
        num = num // 10
    if sum == prod:
        print("the sum and product are same")
    else:
        print("the sum and product are not same")
if __name__ == "__main__":
    fun()

    
