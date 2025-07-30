def fun():

    a=[]
    print("Type 9 values (0s or 1s)")
    for i in range(3):
        b=[]
        for j in range(3):
            b.append(int(input()))
        a.append(b)
    print("input matrix is \n")
    for n in a:
        for m in n:
            print(m,end=" ")
        print()
    flag=True
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (i==j) and (a[i][j]!=1):
                flag=False
                break
            elif (i!=1) and (a[i][j]!=0):
                flag=False
                break
    if flag==True:
        print("Unit Matrix")
    else:
        print("Not Unit Matrix")
if __name__=="__main__":
    fun()
    