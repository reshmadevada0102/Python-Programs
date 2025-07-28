def row(r):
    if r <= 5:
        col(1)
        print()
        row(r + 1)
def col(c):
    if c <= 5:
        print(c,end=' ')
        col(c + 1)
row(1)
