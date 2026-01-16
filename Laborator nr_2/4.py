# Задача 4. Să se elaboreze un program care să citească de la tastatură două numere reale a și b, apoi să pună utilizatorului întrebarea: Ce doriți să calculați, media aritmetică sau geometrică? Dacă se va răspunde prin 1, se va calcula și afișa media aritmetică a numerelor, iar pentru 2 – media geometrică (numai în cazul numerelor pozitive). Dacă nu se răspunde prin 1 sau 2 se va afișa ‘Răspuns incorect’.
a=float(input("Введите a: "))
b=float(input("Введите b: "))
print("Что желаете вычислить?")
print("Нажмите 1, если среднее арифметическое значение")
print("Нажмите 2, если среднее геометрическое значение")
r=int(input("Ваш ответ: "))

if r==1:
    m=(a+b)/2
    print("Среднее арифметическое значение:", m)
else:
    if r==2:
        if a>0 and b>0:
            m=(a*b)**0.5
            print("Среднее геометрическое значение:", m)
        else:
            print("Ошибка: отрицательные значения чисел")
    else:
        print("Ответ неверный")