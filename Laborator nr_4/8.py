# Задача 8. Să se elaboreze un program care calculează suma S=1+1*2+1*2*3+..+1*2*..*n.
n=int(input("Введите n: "))

suma=0
produs=1
i=1
while i<=n:
    produs=produs*i
    suma=suma+produs
    i=i+1
print("Сумма:", suma)