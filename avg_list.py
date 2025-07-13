def main():
    arr=[10,20,30,40,50]
    print("original array")
    print(arr)
    print(f"average is {average(arr)}")

def average(a: list)->float:
    sum=0
    # for i in range(0,len(a)):
    for n in a:
        sum = sum + n
    return sum / len(a)

if __name__=="__main__":
    main()