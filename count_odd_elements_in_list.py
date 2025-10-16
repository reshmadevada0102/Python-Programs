'''WAP to count odd elements in a list'''
def main():
    a = [2,3,5,4,7,6,8,9,1,2]
    count = 0
    for i in range(0, len(a)):
        if a[i] % 2 == 0:
            pass
        else:
            count = count + 1
    print(f"There are {count} odd elements")
if __name__ == "__main__":
    main()