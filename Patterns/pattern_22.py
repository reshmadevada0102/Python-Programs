'''
1 0 0 0 1 
0 1 0 1 0 
0 0 1 0 0 
0 1 0 1 0 
1 0 0 0 1 
'''

def pattern():
    for i in range(1,6):
        for j in range(1,6):
            if (i == j) or (i + j == 6):
                print('1', end= " ")
            else:
                print('0', end= " ")
        print()
pattern()