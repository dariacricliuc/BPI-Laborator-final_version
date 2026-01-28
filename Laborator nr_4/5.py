# Задача 5. Să se elaboreze un program care citește un șir de n numere reale și afișează valoarea minimă și cea maximă din acest șir.
n=int(input("Введите количество чисел: "))
x=float(input("Введите первое число: "))

minim=x
maxim=x
i=1
while (i<n):
    x=float(input("Введите следующее число: "))
    if x<minim:
        minim=x
    if x>maxim:
        maxim=x
    i=i+1
print("Минимальное значение:", minim)
print("Максимальное значение:", maxim)