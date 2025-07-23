def week_day(n:int)->None:
    match n:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")

        case _:
            print("Invalid weekday code")
def main():
    week_day(4)
if __name__ == "__main__":
    main()