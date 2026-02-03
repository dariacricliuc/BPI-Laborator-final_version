# Задача 4. De la tastatură se introduc 3 numere reale a, b și c. Să se elaboreze un program care calculează valoarea expresiei MAX(a-b, a, a+b)+MAX(a, b+c, a-c), utilizând funcția MAX.
def MAX(x, y, z):
    if x>=y and x>=z:
        return x
    elif y>=z:
        return y
    else:
        return z

a=float(input("Введите a: "))
b=float(input("Введите b: "))
c=float(input("Введите c: "))

rezultat=MAX(a-b, a, a+b)+MAX(a, b+c, a-c)
print("Результат:", rezultat)