def fun(*args):  #*args allows the function to accept any number of non-keyword(positional) arguments
    Sum = 0
    for i in args: #iterates through each element
        Sum = Sum + i
    print(Sum)
fun(2, 6, 7, 1)
fun(1,2,3,4)