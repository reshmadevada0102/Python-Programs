def calc(a,b):
    sum = a+b
    sub = a-b
    mult = a*b
    div = a/b
    return sum, sub, mult, div
t = calc(100,50)
print("The results are:")
for i in t:
    print(i)
    