# Задача 6. Să se elaboreze un program care afișează câte cifre pare și câte impare are un număr întreg.
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
print("Нечётных цифр:", n)