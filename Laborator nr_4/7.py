# Задача 7. De la tastatură se introduc 10 numere întregi. Să se elaboreze un program care determină și afișează: numărul celor pozitive și suma lor; media aritmetică а celor negative.
count_poz=0
suma_poz=0
suma_neg=0
count_neg=0
i=1
while i<=10:
    numar=int(input("Введите целое число: "))
    if numar>0:
        count_poz=count_poz+1
        suma_poz=suma_poz+numar
    else:
        if numar<0:
            count_neg=count_neg+1
            suma_neg=suma_neg+numar
    i=i+1
print("Позитивные числа:", count_poz)
print("Сумма позитивных чисел:", suma_poz)

if count_neg>0:
    media_neg=suma_neg/count_neg
    print("Среднее значение негативных чисел:", media_neg)
else:
    print("Негативных чисел нет")