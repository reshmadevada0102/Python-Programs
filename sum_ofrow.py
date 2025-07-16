def main():
    row_sum=[0]
    a=[[4,3,7],[8,6,1,4,9],[2,5,5,3]]
    print("Matrix is")
    for n in a:
        for m in n:
            print(m,end=" ")
        print()
    print("sum of each row")
    for i in range(len(a)):
        row_sum=sum(a[i])
        print(f"sum of row {i+1} is {row_sum}")
    print()
if __name__=="__main__":
    main()