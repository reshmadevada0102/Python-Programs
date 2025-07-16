def fact(n:int)->int:
    result=1
    for i in range(1,n+1):
        result=result * i
    return result
def main():
    n=int(input("enter an integer:"))
    print(f"factorial of {n} is {fact(n)}")
if __name__=="__main__":
    main()
