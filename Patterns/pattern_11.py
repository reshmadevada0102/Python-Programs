def pattern()->None:
    for i in range(5,0,-1):
        for j in range(5,i-1,-1):
            print(j,end=" ")      
        print()
def main():
    pattern()
if __name__=="__main__":
    main()