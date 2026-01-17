# Задача 7. Fie a, b, c, d numere întregi citite de la tastatură. Să se elaboreze un program care să calculeze suma primelor două dacă c<d, produsul lor dacă c>d și suma inverselor, dacă c=d.
a=int(input("Введите a: "))
b=int(input("Введите b: "))
c=int(input("Введите с: "))
d=int(input("Введите d: "))

if c<d:
    r=a+b
    print("Сумма первых двух чисел:", r)
else:
    if c>d:
        r=a*b
        print("Произведение первых двух чисел:", r)
        
if a!=0 and b!=0:
    r=1/a+1/b
    print("Сумма первых двух обратных чисел:", r)
else:
    print("Ошибка: деление на ноль")