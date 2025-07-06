def sqr_ser(n:int)-> None:
    for x in range(1,n+1):
        print(x**2,end=" ")
def main():
    n=int(input("enter an integer"))
    sqr_ser(n)
if __name__=="__main__":
    main()