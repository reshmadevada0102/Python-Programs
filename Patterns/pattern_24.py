'''
☻ 
☻ ♥ 
☻ ♥ ♦ 
☻ ♥ ♦ ♣ 
☻ ♥ ♦ ♣ ♠ 
'''

def pattern():
    for i in range(1,6):
        for j in range(1, i+1):
            print(chr(j+1), end= " ")
        print()
pattern()