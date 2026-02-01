# Задача 4. Se introduc de la tastatură un șir de numere întregi până la 0 (nenule). Să se elaboreze un program care determină numărul elementelor de trei cifre.
count=0
while True:
    x=int(input("Введите число: "))
    if x==0:
        break
    if 100<=x<=999:
        count=count+1
print("Количество трёхзначных чисел:", count)