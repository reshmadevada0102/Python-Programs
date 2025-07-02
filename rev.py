def main():
    arr=[10,0,30,40,50]
    print("original array")
    for n in arr:
        print(n,end=" ")
    rev(arr)

    #arr.reverse()
    print("\n\nReverse array")
    for n in arr:
        print(n,end=" ")

def rev(a:list) -> None:
    for i in range(0,len(a)//2):
        a[i], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[i]

if __name__ == "__main__":
    main()