# Задача 6. Să se elaboreze un program care afișează toate numerele de 3 cifre, suma cifrelor cărora este divizibilă prin 5.
x=100
while (x<=999):
    a=x//100          
    b=(x//10)%10   
    c=x%10
    s=a+b+c
    if (s%5==0):
        print("Сумма цифр числа кратна пяти")
    else:
        print("Сумма цифр числа не кратна пяти")
    x=x+1