import math
import cmath 
import time
i = 0
a = "aaa"
def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False
while is_digit(a) == False:
    a = input("Введите число: ")
a = float(a)
t1 = time.time() 
while i < 1000000:
    math.sqrt(a)
    i += 1
i = 0
t2 = time.time()      
sqrt1 = t2 - t1

t1 = time.time() 
while i < 1000000:
    cmath.sqrt(a)
    i += 1
i = 0
t2 = time.time()  
sqrt2 = t2 - t1 

t1 = time.time() 
while i < 1000000:
    cmath.sin(a)
    i += 1
i = 0
t2 = time.time()  
sin1 = t2 - t1 

t1 = time.time() 
while i < 1000000:
    cmath.sin(a)
    i += 1
i = 0
t2 = time.time()  
sin2 = t2 - t1
print('Math sqrt:', sqrt1, 'Cmath sqrt:', sqrt2, "|| " 'Math sin:', sin1, 'Cmath sin:', sin2)

if max(sqrt1, sqrt2) == sqrt2:
    print("Скорость вычисления квадратного корня быстрее у Cmath на ", sqrt2 - sqrt1)
else:
    print("Скорость вычисления квадратного корня быстрее у Math на ", sqrt1 - sqrt2)

if max(sin1, sin2) == sin2:
    print("Скорость вычисления синуса быстрее у CMath на ", sin2 - sin1)
else:
    print("Скорость вычисления синуса быстрее у Math на ", sin1 - sin2)

