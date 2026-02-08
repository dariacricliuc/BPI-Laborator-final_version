# Задача 6. Se cunosc următoarele date despre cărțile unei librării: titlul, autorul, anul apariției. Să se formeze un tabel cu informații despre n (n<=100) cărți și să se afișeze: lista autorilor în ordine alfabetică; lista cuprinzând autorii și cărțile lor în ordinea anilor de apariție; titlurile cărților publicate de autorul X (citit de la tastatură) după anul 1989.
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
    i=i+1