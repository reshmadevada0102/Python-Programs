'''
1 0 0 0 0 
0 1 0 0 0 
0 0 1 0 0 
0 0 0 1 0 
0 0 0 0 1 
'''

def row(r):
    if r <= 5:
        col(r,1)
        print()
        row(r+1)
def col(r,c):
    if c <= 5:
        if r == c:
            print(1, end= " ")
        else:
            print(0, end=" ")
        col(r, c+1)
def main():
    row(1)
if __name__ == "__main__":
    main() 