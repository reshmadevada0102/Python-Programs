def count(list, index):
    if index == len(list):
        return 0
    else:
        return list[index] % 2 + count(list, index + 1)
    
def main():
    a = [2,7,5,3,7,6,8,9,4,1]
    print("list is :", a)
    print(f"There are {count(a,0)} odd numbers")

if __name__ == "__main__":
    main()