# Задача 5. Se citește un număr natural X format din 4 cifre. Să se afișeze numărul obținut din suma numerelor care se obțin eliminând pe rând prima cifră a lui X, apoi primele două, apoi primele trei. Exemplu: Dacă X=2347 se obține 347+47+7=401.
x=int(input("Введите четырёхзначное натуральное число: "))
s=x%1000+x%100+x%10
print(x%1000, "+", x%100, "+", x%10, "=", s)