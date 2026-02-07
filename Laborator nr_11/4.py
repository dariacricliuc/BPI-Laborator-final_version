# Задача 4. Se citește o matrice A cu n linii și m coloane (n<=30, m<=30) cu elemente numere întregi. Scrieți un program care determină și afișează: elementul minim de pe fiecare linie; elementul maxim de pe fiecare coloană.
n=int(input("Введите количество строк: "))
m=int(input("Введите количество столбцов: "))

A=[[0]*m for _ in range(n)]
i=0
while i<n:
    j=0
    while j<m:
        A[i][j]=int(input("Введите число:" ))
        j=j+1
    i=i+1
i=0
while i<n:
    min_lin=A[i][0]
    j=1
    while j<m:
        if A[i][j]<min_lin:
            min_lin=A[i][j]
        j=j+1
    print("Минимальный элемент в строке:", min_lin)
    i=i+1
j=0
while j<m:
    max_col=A[0][j]
    i=1
    while i<n:
        if A[i][j]>max_col:
            max_col=A[i][j]
        i=i+1
    print("Максимальный элемент в столбце:" ,max_col)
    j=j+1