# Задача 4. Se cunosc următoarele date despre angajații unei firme: nume, prenume, salariu, avans. Să se formeze un tabel cu informații despre n (n<=100) angajați și să se afișeze: suma de bani cât mai are de primit fiecare angajat; angajații firmei în ordine crescătoare în funcție de salariu; salariul mediu pe firmă.
n=int(input("Введите количество рабочих: "))

angajati=[()]*n
i=0
while i<n:
    nume=input("Фамилия: ")
    prenume=input("Имя: ")
    salariu=float(input("Зарплата: "))
    avans=float(input("Аванс: "))
    angajati[i]=(nume, prenume, salariu, avans)
    i=i+1
print("Оставшаяся сумма:")
i=0
while i<n:
    ramas=angajati[i][2]-angajati[i][3]
    print(angajati[i][0], angajati[i][1], ":", ramas)
    i=i+1
i=0
while i<n-1:
    j=i+1
    while j<n:
        if angajati[i][2]>angajati[j][2]:
            angajati[i], angajati[j]=angajati[j], angajati[i]
        j=j+1
    i=i+1
print("Рабочие в порядке возрастания:")
i=0
while i<n:
    print(angajati[i][0], angajati[i][1], ":", angajati[i][2])
    i=i+1
total=0
i=0
while i<n:
    total+=angajati[i][2]
    i=i+1
medie=total/n
print("Средняя зарплата:", medie)