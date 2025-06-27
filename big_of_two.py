def big_of_two(a,b):
    if a>b:
        return a
    else:
        return b
def main():
    x=int(input("Enter an integer:"))
    y=int(input("Enter another integer:"))
    print(f"{big_of_two(x,y)} is big")
if __name__=="__main__":
    main()