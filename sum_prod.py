def is_same(n: int)->bool:
    sum = 0
    prod = 1
    while n>0:
        sum = sum + n % 10
        prod = prod * n % 10
        n = n // 10

    return True if sum==prod else False

def fun():
    n=int(input("enter an integer"))
    if is_same(n)==True:
        print("Sum and Product are same")
    else:
        print("Sum and product are not same")
if __name__ == "__main__":
    fun()