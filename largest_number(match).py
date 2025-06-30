def biggest(a:int, b:int) -> int:
    match(a > b):
        case True:
            print(f"{a} is bigger")
        case False:
            print(f"{b} is bigger")

def main():
    a=int(input("Enter an integer:"))
    b=int(input("Enter another integer:"))
    biggest(a, b)

main()