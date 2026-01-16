# Задача 6. Să se elaboreze un program care să citească data curentă (zi, lună, an) și să determine data zilei următoare.
d=int(input("Введите день: "))
m=int(input("Введите месяц: "))
g=int(input("Введите год: "))

match m:
    case 1|3|5|7|8|10|12:
        total=31
    case 4|6|9|11:
        total=30
    case 2:
        if g%4==0:
            total=29
        else:
            total=28
    case _:
        print("Неверно введённый месяц")
        exit()

d=d+1
if d>total:
    d=1
    m=m+1
    if m>12:
        m=1
        g=g+1
print("Дата следующего дня:", d, m, g)