# Задача 4. Să se elaboreze un program care completează un vector A cu n numere întregi citite de la tastieră și determină numărul de elemente vecine cu semn opus.
n=int(input("Введите количество чисел: "))

A=[0]*n
i=0
while i<n:
    A[i]=int(input("Введите число: "))
    i=i+1
count=0
i=1
while i<n:
    if (A[i-1]>0 and A[i]<0) or (A[i-1]<0 and A[i]>0):
        count=count+1
    i=i+1
print("Количество соседних элементов с противоположными знаками:", count)