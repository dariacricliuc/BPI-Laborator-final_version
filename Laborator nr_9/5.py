# Задача 5. Să se elaboreze un program care citește de la tastieră un număr întreg k, completează un vector A cu n numere întregi citite de la tastieră și determină poziția primului element din tabloul mai mare decât k.
k=int(input("Введите k: "))
n=int(input("Введите количество чисел: "))

A=[0]*n
i=0
while i<n:
    A[i]=int(input("Введите число: "))
    i=i+1
gasit=False
i=0
while i<n:
    if A[i]>k:
        print("Первый элемент больше, чем", k, "находится на позиции", i+1)
        gasit=True
        break
    i=i+1
if not gasit:
    print("Элементов больше, чем", k, "не существует")