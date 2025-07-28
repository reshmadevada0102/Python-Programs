def row(r):
    if r <= 5:
        col(r,1)
        print()
        row(r + 1)
def col(r,c):
    if c <= 5:
        print(r,end=' ')
        col(r,c + 1)
row(1)
