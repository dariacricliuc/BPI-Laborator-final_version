# Задача 7. Alexandra a economisit S lei și vrea să depoziteze această sumă la o bancă cu o dobânda de P% pe an, pe un termen de 3 luni. Să se afișeze dobânda obținută de Alexandra după 3 luni. Valorile S și P sunt numere naturale citite de la tastatură.
S=int(input("Введите сумму сэкономленных Александрой леев: "))
P=int(input("Введите годовой процент: "))
x=(S*P)/400
print("Сумма процентов за три месяца составляет:", x, "леев")