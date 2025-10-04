'''
1 2 3 4 5 
2 3 4 5 6 
3 4 5 6 7 
4 5 6 7 8 
5 6 7 8 9 
'''

def row(r):
    if r <= 5:
        col(r,1)
        print()
        row(r + 1)
def col(r, c):
    if c <= 5:
        print(r,end=' ')
        col(r + 1, c + 1)
row(1)