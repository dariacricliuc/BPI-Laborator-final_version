# Задача 11. Să se elaboreze un program care afișează toate numerele de 3 cifre, care sunt egale cu diferența dintre pătratul numărului alcătuit din primele 2 cifre și pătratul ultimei cifre. Exemplu: Date de intrare: n=147, Date de ieşire: 14*14–7*7=147.
numar=100
while numar<=999:
    primele_doua=numar//10
    ultima=numar%10  
    diferenta=primele_doua*primele_doua-ultima*ultima
    if diferenta==numar:
        print(primele_doua, "*", primele_doua, "-", ultima, "*", ultima, "=", numar)
    numar=numar+1