# Задача 5. Să se elaboreze un program care afișează numărul de cifre a unui număr.
x=int(input("Введите число: "))

x=abs(x)
count=0
if (x==0):
    count=1
else:
    while (x>0):
        x=x//10
        count=count+1
print("Количество цифр:", count)