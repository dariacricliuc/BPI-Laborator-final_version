# Задача 1. Să se scrie un program care citește un număr de ani și calculează numărul de luni, zile și ore corespunzătoare. Se consideră că un an are 365 zile. Exemplu: Date de intrare: 2. Date de ieșire: 24 luni 730 zile 17520 ore.
y=int(input("Введите количество лет: "))
if y>=0:
    m=y*12
    d=y*365
    h=d*24
    print('Количество лет: ', y)
    print('Количество месяцев: ', m)
    print('Количество дней: ', d)
    print('Количество часов: ', h)
else:
    print("Ошибка: количество лет не может быть отрицательным числом")