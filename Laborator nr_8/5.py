# Задача 5. Să se elaboreze un program care completează un vector A cu n numere întregi citite de la tastieră și calculează produsul valorilor impare situate pe poziții pare.
n=int(input("Введите количество чисел: "))

A=[0]*n
i=0
while i<n:
    A[i]=int(input("Введите число: "))
    i=i+1
produs=1
i=0
while i<n:
    if i%2==0 and A[i]%2==1:
        produs=produs*A[i]
    i=i+1
print("Произведение нечётных значений на чётных позициях:", produs)