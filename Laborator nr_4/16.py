# Задача 16. Se consideră „fericit” biletul de 6 cifre, dacă suma primelor 3 cifre a căruia este egală cu suma ultimelor 3 cifre. Să se elaboreze un program care afișează toate numerele fericite.
numar=100000
while numar<=999999:
    cifra1=numar//100000
    cifra2=(numar//10000)%10
    cifra3=(numar//1000)%10
    cifra4=(numar//100)%10
    cifra5=(numar//10)%10
    cifra6=numar%10
    suma_primele=cifra1+cifra2+cifra3
    suma_ultimele=cifra4+cifra5+cifra6
    if suma_primele==suma_ultimele:
        print(numar)
    numar=numar+1