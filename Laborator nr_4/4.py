# Задача 4. Să se elaboreze un program care afișează numerele de două cifre care au ultima cifră divizibilă cu 3.
x=10 
while (x<=99):
    c=x%10
    if (c%3==0):
        print("Последняя цифра данного числа кратна трём")
    else:
        print("Последняя цифра данного числа не кратна трём")
    x=x+1