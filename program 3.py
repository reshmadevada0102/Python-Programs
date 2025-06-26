def fun3():
    x=10
    y=20
    print(f"x is {x} and y is {y}")
    x,y=y,x
    print("x=",x)
    print("y=",y)
fun3()