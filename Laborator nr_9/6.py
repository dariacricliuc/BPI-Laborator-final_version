# Задача 6. Să se elaboreze un program care completează un vector A cu n numere naturale citite de la tastieră și determină poziția ultimului element egal cu 0.
n=int(input("Введите количество чисел: "))

A=[0]*n
i=0
while i<n:
    A[i]=int(input("Введите число: "))
    i=i+1
gasit=False
i=n-1
while i>=0:
    if A[i]==0:
        print("Последний элемент, равный 0, находится на позиции", i+1)
        gasit=True
        break
    i=i-1
if not gasit:
    print("Элементов, равных 0, не существует")