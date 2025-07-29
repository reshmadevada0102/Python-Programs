def fibo(pp,p,count):
    if count <= 10:
        print(p + pp,end=' ')
        fibo(p, p + pp, count + 1)
def main():
    a = 0
    b = 1
    print(a, b)
    fibo(a, b, 1,)
if __name__ == "__main__":
    main()