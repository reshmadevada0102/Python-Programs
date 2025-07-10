def pattern()->None:
    for i in range(1,6):
        for j in range(1,5-i+1,+1):
            print(' ',end=" ")
        for j in range(1,2*i):
            print('*',end=" ")
        print()
def main():
    pattern()
if __name__=="__main__":
    main()