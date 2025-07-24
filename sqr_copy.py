def main():
    b=[]
    a=[]
    n=int(input("Enter number"))
    print(f"Type {n} elements:")
    for i in range(n):
        a.append(int(input()))
    sqr_copy(a,b)
    print(b)

def sqr_copy(x:list,y:list)->None:
    for i in range(len(x)):
        y.append(x[i]**2)
    
if __name__=="__main__":
    main()