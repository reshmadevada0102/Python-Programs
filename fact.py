def fact(n:int)->int:
    result=1
    for i in range(n,1,n-1):
        result=(i*i)
    return result
def main():
    n=int(input("enter an integer:"))
    print(f"factorial of {n} is {fact(n)}")
if __name__=="__main__":
    main()
