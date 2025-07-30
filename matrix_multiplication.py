def fun():
    a=[[1,2,3],[4,5,6]]
    b=[[2, 1, 5, 8],[4,5, 4,6],[7,1, 1, 9]]
    c = []
    print("1st matrix is")
    for rows in a:
        for elements in rows:
            print(elements,end=" ")
        print()
    print("2nd matrix is")
    for rows in b:
        for elements in rows:
            print(elements,end=" ")
        print()
    for i in range(len(a)):
        d = []
        for j in range(len(b[0])):
            temp = 0
            for k in range(len(b)):
                temp += (a[i][k]*b[k][j])
            d.append(temp)
        c.append(d)

    print("Result matrix is")
    for rows in c:
        for elements in rows:
            print(elements,end=" ")
        print()

if __name__ == '__main__':
    fun()
