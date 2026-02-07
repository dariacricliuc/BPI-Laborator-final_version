# Задача 5. Scrieți un program care citește de la tastatură un număr natural n (2<n<20), construiește în memorie și afișează pe ecran o matrice cu n linii și n coloane, care memorează pe prima linie valorile de la 1 la n, apoi pe următoarele linii permutările circulare la stânga a șirului 1,2,3,..,n. Exemplu: pentru n=5 se va afișa matricea: (1 2 3 4 5) (2 3 4 5 1) (3 4 5 1 2) (4 5 1 2 3) (5 1 2 3 4).
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
    i=i+1