def rev_of_num(n:int)-> int:
    rev=0
    while n>0:
        rev=rev*10+n%10
        n=n//10
    return rev
def main():
    num=int(input("Enter an integer:"))
    print(f"Reverse of number {num} is {rev_of_num(num)}")
if __name__=="__main__":
    main()