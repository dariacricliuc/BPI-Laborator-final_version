# Задача 5. Se cunosc rezultatele obținute la examenul de admitere la liceu: nume, prenume și notele obținute de către fiecare elev la cele doua probe de examen. Să se formeze un tabel cu informații despre n (n<=100) elevi și să se afișeze: lista candidaților admiși la acest examen în ordine descrescătoare a mediilor obținute, știind că numărul de locuri este 50, iar media minimă la admitere este 5.00; lista elevilor respinși în ordine alfabetică.
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
    i=i+1