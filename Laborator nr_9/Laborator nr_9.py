'''# Задача 4. Să se elaboreze un program care completează un vector A cu n numere naturale citite de la tastieră și determină dacă toate componentele vectorului aparțin intervalului [1; m].
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
    print("Все числа не находятся в интервале от 1 до", m)'''



'''# Задача 5. Să se elaboreze un program care citește de la tastieră un număr întreg k, completează un vector A cu n numere întregi citite de la tastieră și determină poziția primului element din tabloul mai mare decât k.
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
    print("Элементов больше, чем", k, "не существует")'''



'''# Задача 6. Să se elaboreze un program care completează un vector A cu n numere naturale citite de la tastieră și determină poziția ultimului element egal cu 0.
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
    print("Элементов, равных 0, не существует")'''