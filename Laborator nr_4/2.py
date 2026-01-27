# Задача 2. Se citesc numerele n și k de la tastatură și apoi n–numere naturale pe rând. Să se elaboreze un program care afișează acele numere dintre cele n introduse care au exact k divizori.
n=int(input("Введите количество чисел: "))
k=int(input("Введите количество делителей: "))

i=1
result=""
while i<=n:
    x=int(input("Введите число: "))
    divisors=0
    j=1
    while j*j<=x:
        if x%j==0:
            if j*j==x:
                divisors=divisors+1
            else:
                divisors=divisors+2
        j=j+1
    if divisors==k:
        if result=="":
            result=str(x)
        else:
            result=result+" "+str(x)
    i=i+1
    
if result=="":
    print("Нет чисел с", k, "делителями")
else:
    print("Числа с", k, "делителями:", result)