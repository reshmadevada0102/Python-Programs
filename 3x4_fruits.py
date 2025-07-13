def main():
    a=[]
    print("enter 12 fruits name")
    for i in range(3):
        b=[]
        for j in range(4):
            b.append((input()))
        a.append(b)
    print(a)
    for i in range(3):
        for j in range(4):
            print(a[i][j],end=" ")
        print()
if __name__ == "__main__":
    main()
