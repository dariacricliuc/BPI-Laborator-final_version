# Задача 14. Se citesc n numere întregi, pe rând într-o variabilă x şi o valoare întreagă a. Să se elaboreze un program care determină numărul de apariții ale valorii a, printre numerele citite.
n=int(input("Введите количество чисел: "))
a=int(input("Введите значение: "))

count=0
i=1
while i<=n:
    x=int(input("Введите число: "))
    if x==a:
        count=count+1
    i=i+1
print("Значение", a, "появляется", count, "раз")