def main():
    arr=[20,10,40,30,60,50,90,80,70,100]
    print("original array")
    print(arr)
    rsort(arr)
    print("sorted array")
    print(arr)
def rsort(a: list)->None:
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[j] < a[i]:
                a[i],a[j]=a[j],a[i]
if __name__=="__main__":
    main()