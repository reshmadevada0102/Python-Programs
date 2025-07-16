def ser(n:int)->int:
    x=0
    for i in range(1,n+1):
        x=x+(i*i)
        print(x,end=" ")
def main():
    n=int(input("enter the integer:"))
    ser(n)
if __name__=="__main__":
    main()