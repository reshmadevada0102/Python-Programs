def pattern()->None:
    for i in range(1,6):
        for j in range(1,i+1):
            print(j,end=" ")      
        print()
def main():
    pattern()
if __name__=="__main__":
    main()