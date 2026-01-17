# Задача 8. Să se elaboreze un program care să citească un număr X natural din exact 3 cifre și să determine: dacă suma cifrelor numărului X reprezintă un număr din exact 2 cifre; dacă produsul cifrelor numărului X reprezintă un număr din exact 3 cifre; dacă produsul cifrelor numărului X este mai mare decât însuși numărul X; dacă suma cifrelor numărului X este divizibilă cu numărul Y.
X=int(input("Введите натуральное трёхзначное число: "))
Y=int(input("Введите число Y: "))
s=X//100
d=(X//10)%10
e=X%10
suma=s+d+e
pr=s*d*e

if 10<=suma<=99:
    print("Сумма цифр является двухзначным числом")
else:
    print("Сумма цифр не является двухзначным числом")
    
if 100<=pr<=999:
    print("Произведение цифр является трёхзначным числом")
else:
    print("Произведение цифр не является трёхзначным числом")

if pr>X:
    print("Произведение цифр больше самого числа Х")
else:
    print("Произведение цифр меньше самого числа Х")

if Y!=0:
    if suma%Y==0:
        print("Сумма цифр кратна числу", Y)
    else:
        print("Сумма цифр не кратна числу", Y)
else:
    print("Ошибка: деление на ноль")