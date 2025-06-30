def big_in_three(a, b, c):
    match (a>b and a>c):
        case True:
            print("A is big")
        case False:
            match (b>a and b>c):
                case True:
                    print("B is big")
                case False:
                    print("C is big")

big_in_three(10, 9, 17)

