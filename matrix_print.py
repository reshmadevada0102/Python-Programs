def fun():
    a = [[1,2,3], [4, 5, 6], [7, 8, 9], [3, 3, 3]]

    print(a)

    print(a[0])
    print(a[1])
    print(a[2])

    print(a[2][1])

    print("Matrix altogether\n")
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end = " ")
        print()


    print("Matrix altogether in different wa\n")
    for i in a:
        for j in i:
            print(j, end = " ")
        print()

fun()

