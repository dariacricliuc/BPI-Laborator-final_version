# Задача 12. Este dat un număr natural N. Să se elaboreze un program care calculează câte ore, minute, secunde sunt în N zile (o zi = 24 ore).
N=int(input("Введите количество дней: "))

if N>=0:
    h=N*24
    m=h*60
    s=m*60
    print("Количество дней:", N)
    print("Количество часов:", h)
    print("Количество минут:", m)
    print("Количество секунд:", s)
else:
    print("Ошибка: количество дней не может быть отрицательным числом")