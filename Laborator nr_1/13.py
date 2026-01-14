# Задача 13. Elevul dorește să înscrie pe o dischetă 3 fișiere de dimensiuni X, Y, Z Kb. Volumul dischetei este de 1,41Mb. De câte dischete are nevoie elevul?
print("Объём диска равен 1,41Mb")
x=float(input("Введите размер первого файла: "))
y=float(input("Введите размер второго файла: "))
z=float(input("Введите размер третьего файла: "))
d=1410
s=x+y+z
n=s//d

if n>0:
    print("Всего необходимо:", n, "дисков")
else:
    if n==0:
        print("Новые диски не нужны")
    else:
        print("Ошибка: количество дисков не может быть отрицательным числом")