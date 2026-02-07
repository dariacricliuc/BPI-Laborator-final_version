# Задача 6. Se citește o matrice A cu n linii și m coloane (n<=30, m<=30) cu elemente numere întregi. Scrieți un program care schimbă cu locurile primul rând cu rândul în care apare primul element cu valoarea 0.
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
    i=i+1