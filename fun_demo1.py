def fun(x,y = 20):  #the value of x is not initialized
    print(f"x+y is {x+y}")
def main():
    fun(40,y = 60)  #the first value 40 is the value of x and the value of y is updated from 40 to 60
main()