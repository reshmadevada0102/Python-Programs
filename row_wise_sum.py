def read_mat():
    mat = []
    n=3
    print(f"Type {(n*n)} elements for {n}x{n} matrix")
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(int(input()))
        mat.append(temp)
    print('Matrix is')
    for i in range(3):
        for j in range(3):
            print(mat[i][j], end=" ")
        print()
    for i in range(3):
        sum = 0
        for j in range(3):
            sum = sum + mat[i][j]
        print(f"Sum of elements in row {i+1} is {sum}")
read_mat()
