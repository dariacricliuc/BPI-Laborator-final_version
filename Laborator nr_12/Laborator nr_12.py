'''# Задача 4. Se cunosc următoarele date despre angajații unei firme: nume, prenume, salariu, avans. Să se formeze un tabel cu informații despre n (n<=100) angajați și să se afișeze: suma de bani cât mai are de primit fiecare angajat; angajații firmei în ordine crescătoare în funcție de salariu; salariul mediu pe firmă.
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
print("Средняя зарплата:", medie)'''



'''# Задача 5. Se cunosc rezultatele obținute la examenul de admitere la liceu: nume, prenume și notele obținute de către fiecare elev la cele doua probe de examen. Să se formeze un tabel cu informații despre n (n<=100) elevi și să se afișeze: lista candidaților admiși la acest examen în ordine descrescătoare a mediilor obținute, știind că numărul de locuri este 50, iar media minimă la admitere este 5.00; lista elevilor respinși în ordine alfabetică.
n=int(input("Введите количество учеников: "))

elevi=[()]*n
i=0
while i<n:
    nume=input("Фамилия: ")
    prenume=input("Имя: ")
    nota1=float(input("Оценка 1: "))
    nota2=float(input("Оценка 2: "))
    media=(nota1+nota2)/2
    elevi[i]=(nume, prenume, nota1, nota2, media)
    i=i+1
respinși=[()]*n
count_respinsi=0
i=0
while i<n:
    if elevi[i][4]<5.00:
        respinși[count_respinsi]=elevi[i]
        count_respinsi+=1
    i=i+1
i=0
while i<count_respinsi-1:
    j=i+1
    while j<count_respinsi:
        if respinși[i][0]>respinși[j][0]:
            respinși[i], respinși[j]=respinși[j], respinși[i]
        j=j+1
    i=i+1
print("Задолжники:")
i=0
while i<count_respinsi:
    print(respinși[i][0], respinși[i][1], ":", respinși[i][4])
    i=i+1'''



'''# Задача 6. Se cunosc următoarele date despre cărțile unei librării: titlul, autorul, anul apariției. Să se formeze un tabel cu informații despre n (n<=100) cărți și să se afișeze: lista autorilor în ordine alfabetică; lista cuprinzând autorii și cărțile lor în ordinea anilor de apariție; titlurile cărților publicate de autorul X (citit de la tastatură) după anul 1989.
n=int(input("Введите количество книг: "))

carti=[()]*n
i=0
while i<n:
    titlu=input("Название: ")
    autor=input("Автор: ")
    an=int(input("Год: "))
    carti[i]=(titlu, autor, an)
    i=i+1
print("Авторы в алфавитном порядке:")
autori=[""]*n
i=0
while i<n:
    autori[i]=carti[i][1]
    i=i+1
i=0
while i<n-1:
    j=i+1
    while j<n:
        if autori[i]>autori[j]:
            autori[i], autori[j]=autori[j], autori[i]
        j=j+1
    i=i+1
i=0
while i<n:
    if i==0 or autori[i]!=autori[i-1]:
        print(autori[i])
    i=i+1
print("Авторы и книги по годам:")
i=0
while i<n-1:
    j=i+1
    while j<n:
        if carti[i][2]>carti[j][2]:
            carti[i], carti[j]=carti[j], carti[i]
        j=j+1
    i=i+1
i=0
while i<n:
    print(carti[i][1], "-", carti[i][0], "(", carti[i][2], ")")
    i=i+1
x=input("Автор X: ")
print("Книги автора", x, "după 1989:")
i=0
while i<n:
    if carti[i][1]==x and carti[i][2]>1989:
        print(carti[i][0])
    i=i+1'''