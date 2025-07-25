def swap(lst):
    lst[0],lst[1] = lst[1],lst[0]
def main():
    a=[10,20]
    print(a)
    swap(a)
    print(a)
if __name__ == "__main__":
    main()