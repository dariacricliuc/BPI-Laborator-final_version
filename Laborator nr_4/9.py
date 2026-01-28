# Задача 9. Să se elaboreze un program care calculează suma S=1–2+3–4+..+(-)n.
n=int(input("Введите n: "))

suma=0
i=1
while i<=n:
    if i%2==1:
        suma=suma+i
    else:
        suma=suma-i
    i=i+1
print("Сумма:", suma)