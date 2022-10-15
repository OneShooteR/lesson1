s = []
i = 0
n = 0
j = 0
c = 0
c1 = 0
c2 = 0
def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
            return False

while float(i) < 3 and float(i) < 5:
    print("Сколько элементов в вашем списке?(3-5) ")
    i = input()
while n < float(i):
    print("Введите элемент списка: ")
    s.append(input())   
    n += 1
print(s)
while j < float(i):
    if isfloat(s[j]) == True and '.' in s[j]:
        c += 1
    if isint(s[j]) == True:    
        c1 += 1
    if isfloat(s[j]) == True and '.' in s[j] or isint(s[j]) == True:
        c2 += 1
    j += 1    
if (float(i) - c) == 0:
    print("в этом списке все элементы типа float") 
if (float(i)- c1) == 0:
    print("в этом списке все элементы типа int")
if (float(i)- c2) == 0:
    print("в этом списке есть элементы типа int И float")    
else:
    print("в этом списке есть элементы типа str")         

   