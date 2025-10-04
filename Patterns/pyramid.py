'''
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
'''

def row(n):
    if n <= 5:
        space(5-n)
        star(2*n-1)
        print()
        row(n+1)
def space(s):
    if s > 0:
        print(' ', end = " ")
        space(s-1)
def star(t):
    if t > 0:
        print('*', end= ' ')
        star(t - 1)
def main():
    row(1)
if __name__ == "__main__":
    main()