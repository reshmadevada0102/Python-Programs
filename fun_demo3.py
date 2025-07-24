def fun(**kwargs): #*kwargs allows a function to accept any number of keyword argument
    for keys in kwargs: #iterates through every key
        print(keys, kwargs[keys]) #prints the key along with its value
fun(name = 'Reshma', age = 20, height = 5.1)
fun(item = 'tomato', cost = 20)
fun(id = 101, name = 'manisha',course = 'PowerBI', duration = '5 months')
