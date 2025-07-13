def main():
    a=[[4,3,7],[8,6,1,4,9],[2,5,5,3]]
    print("Matrix is")
    for n in a:
        for m in n:
            print(m,end=" ")
        print()
    for i in range(len(a)):
        big=a[i][0]
        for j in range(len(a[i])):
            if a[i][j]>big:
                big=a[i][j]
        print(f"Biggest element in row {i+1} is {big}")
if __name__=="__main__":
    main()