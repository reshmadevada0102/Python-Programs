def main():
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    print("original matrix")
    for rows in matrix:
        for elements in rows:
            print(elements,end=" ")
        print()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i>j:
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    print("transposed matrix")
    for rows in matrix:
        for elements in rows:
            print(elements,end=" ")
        print()
if __name__=="__main__":
    main()