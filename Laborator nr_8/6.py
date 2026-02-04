# Задача 6. Să se elaboreze un program care completează un vector A cu n numere întregi citite de la tastieră și ordonează descrescător elementele vectorului până la poziția k (citită de la tastieră) și crescător restul vectorului. La final programul afișează pe ecran vectorul obținut.
n=int(input("Введите количество чисел: "))
k=int(input("Введите позицию k: "))

A=[0]*n
i=0
while i<n:
    A[i]=int(input("Введите число: "))
    i=i+1
i=0
while i<k:
    j=i+1
    while j<k:
        if A[i]<A[j]:
            A[i],A[j]=A[j],A[i]
        j=j+1
    i=i+1
i=k
while i<n:
    j=i+1
    while j<n:
        if A[i]>A[j]:
            A[i],A[j]=A[j],A[i]
        j=j+1
    i=i+1
print("Полученный массив:", A)