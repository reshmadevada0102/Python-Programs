'''
M 
M N 
M N O 
M N O P 
M N O P Q 
'''

def pattern():
    for i in range(1,6):
        for j in range(1, i+1):
            print(chr(j+76), end= " ")
        print()
pattern()