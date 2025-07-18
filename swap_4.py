def fun4():
    x=10
    y=20
    print(f"x is {x} and y is {y}")
    x=(x+y)-(y:=x)
    print(f" x is {x} and y is {y}")
fun4()
