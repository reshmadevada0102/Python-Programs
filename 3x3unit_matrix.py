def main():
    a=[]
    for i in range(3):
        b=[]
        for j in range(3):
            if i ==j:
                b.append(1)
            else:
                b.append(0)
        a.append(b)
    for i in range(3):
        for j in range(3):
            print(a[i][j],end=" ")
        print()
if __name__=="__main__":
    main()