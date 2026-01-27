# Задача 3. Se citește un număr natural n și apoi n numere reale. Să se elaboreze un program care calculează și afișează raportul dintre suma numerelor impare și suma numerelor pare.
n=int(input("Введите количество чисел: "))

count=1
suma_impare=0
suma_pare=0
while count<=n:
    numar=float(input("Введите число: "))
    if numar%2==1:
        suma_impare=suma_impare+numar
    else:
        suma_pare=suma_pare+numar
    count=count+1
if suma_pare!=0:
    raport=suma_impare/suma_pare
    print("Отношение:", raport)
else:
    print("Отношение не вычислимо")