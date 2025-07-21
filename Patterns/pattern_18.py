def pattern()->None:
    for i in range(1,6):
        for j in range(1,5-i+1):
            print(' ',end=" ")
        for j in range(1,i+1):
            print(chr(j+64),end=" ")
        for j in range(i-1,0,-1):
            print(chr(j+64),end=" ")
        print()
def main():
    pattern()
if __name__=="__main__":
    main()