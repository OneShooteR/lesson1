def fun(x = None , y = None, z = None):
    if x == None and y == None and z == None:
        return 'const'
    if z == None:
        return x + y
    if z != None:
        return x * y * z

# Примеры

print(fun())

#print(fun(1.0)) ошибка 

print(fun(1.0,5.0)) 

print(fun(2.0,5,7)) 

#print(fun(2.0,5,7,8,6)) ошибка