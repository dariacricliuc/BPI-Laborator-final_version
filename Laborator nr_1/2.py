# Задача 2. Se citește un număr X format din exact 4 cifre. Să se afișeze numărul care se obține prin eliminarea cifrelor din mijloc.
x=int(input("Введите четырёхзначное натуральное число: "))
y=(x//1000)*10+(x%10)
print("Новое число:", y)