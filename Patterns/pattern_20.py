'''
1 1 1 1 1 
0 0 0 0 0 
1 1 1 1 1 
0 0 0 0 0 
1 1 1 1 1 

'''
def pattern():
    for i in range(1,6):
        for j in range(1,6):
            print(i % 2,end=" ")
        print()
pattern()