'''# Задача 4. Se citește o matrice A cu n linii și m coloane (n<=30, m<=30) cu elemente numere întregi. Scrieți un program care determină și afișează: elementul minim de pe fiecare linie; elementul maxim de pe fiecare coloană.
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
    j=j+1'''



'''# Задача 5. Scrieți un program care citește de la tastatură un număr natural n (2<n<20), construiește în memorie și afișează pe ecran o matrice cu n linii și n coloane, care memorează pe prima linie valorile de la 1 la n, apoi pe următoarele linii permutările circulare la stânga a șirului 1,2,3,..,n. Exemplu: pentru n=5 se va afișa matricea: (1 2 3 4 5) (2 3 4 5 1) (3 4 5 1 2) (4 5 1 2 3) (5 1 2 3 4).
n=int(input("Введите n: "))

matrice=[[0]*n for _ in range(n)]
i=0
while i<n:
    j=0
    while j<n:
        element=(i+j)%n+1
        matrice[i][j]=element
        j=j+1
    i=i+1
i=0
while i<n:
    j=0
    while j<n:
        print(matrice[i][j], end="")
        j=j+1
    print()
    i=i+1'''



'''# Задача 6. Se citește o matrice A cu n linii și m coloane (n<=30, m<=30) cu elemente numere întregi. Scrieți un program care schimbă cu locurile primul rând cu rândul în care apare primul element cu valoarea 0.
n=int(input("Введите количество строк: "))
m=int(input("Введите количество столбцов: "))

A=[[0]*m for _ in range(n)]
i=0
while i<n:
    j=0
    while j<m:
        A[i][j]=int(input("Element: "))
        j=j+1
    i=i+1
rand_zero=-1
i=0
while i<n:
    j=0
    while j<m:
        if A[i][j]==0:
            rand_zero=i
            break
        j=j+1
    if rand_zero!=-1:
        break
    i=i+1
if rand_zero!=-1 and rand_zero!=0:
    j=0
    while j<m:
        temp=A[0][j]
        A[0][j]=A[rand_zero][j]
        A[rand_zero][j]=temp
        j=j+1
i=0
while i<n:
    j=0
    while j<m:
        print(A[i][j], end="")
        j=j+1
    print()
    i=i+1'''