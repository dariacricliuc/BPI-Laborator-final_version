# Задача 14. Se citește un număr natural X format din 4 cifre. Să se afișeze numărul obținut din suma numerelor care se obțin eliminând pe rând ultima cifră a lui X, apoi ultimele două, apoi ultimele trei. Exemplu. Dacă X=2347 se obține 234+23+2=259.
x=int(input("Введите четырёхзначное натуральное число: "))
s=x//10+x//100+x//1000
print(x//10, "+", x//100, "+", x//1000, "=", s)