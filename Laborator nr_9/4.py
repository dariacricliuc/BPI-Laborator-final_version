# Задача 4. Să se elaboreze un program care completează un vector A cu n numere naturale citite de la tastieră și determină dacă toate componentele vectorului aparțin intervalului [1; m].
n=int(input("Введите количество чисел: "))
m=int(input("Введите m: "))

A=[0]*n
i=0
while i<n:
    A[i]=int(input("Введите число: "))
    i=i+1
toate_in_interval=True
i=0
while i<n:
    if A[i]<1 or A[i]>m:
        toate_in_interval=False
    i=i+1
if toate_in_interval:
    print("Все числа находятся в интервале от 1 до", m)
else:
    print("Все числа не находятся в интервале от 1 до", m)