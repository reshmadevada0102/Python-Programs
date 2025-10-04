'''WAP to modify a given non-empty list in such a way, when there are two consecutive elements are odd numbers, then it should store sum of both at first position and absolute of sum of divisons in the second. It should not do anythong to the even number which is consecutive of single odd number.
'''

def list(a):
    a = [3,2,6,7,9,4]
    i = 0
    while i < len(a) - 1:
        if a[i] % 2 != 0 and a[i+1] % 2 != 0:
            sum = a[i] + a[i+1]
            div = abs(a[i] - a[i+1])
            a[i], a[i+1] = sum, div
            i += 2
        else:
            i += 1
    return a
print(list([3,2,6,7,9,4]))

