'''# Задача 4. Se introduc de la tastatură un șir de numere întregi până la 0 (nenule). Să se elaboreze un program care determină numărul elementelor de trei cifre.
count=0
while True:
    x=int(input("Введите число: "))
    if x==0:
        break
    if 100<=x<=999:
        count=count+1
print("Количество трёхзначных чисел:", count)'''



'''# Задача 5. Să se elaboreze un program care afișează numărul de cifre a unui număr.
x=int(input("Введите число: "))

x=abs(x)
count=0
if (x==0):
    count=1
else:
    while (x>0):
        x=x//10
        count=count+1
print("Количество цифр:", count)'''



'''# Задача 6. Să se elaboreze un program care afișează câte cifre pare și câte impare are un număr întreg.
x=int(input("Введите число: "))

p=0
n=0
if (x==0):
    p=1
else:
    while (x>0):
        c=x%10
        if (c%2==0):
            p=p+1
        else:
            n=n+1
        x=x//10
print("Чётных цифр:", p)
print("Нечётных цифр:", n)'''