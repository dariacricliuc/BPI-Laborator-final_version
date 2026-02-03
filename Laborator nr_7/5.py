# Задача 5. Să se elaboreze un program care afișează toate numerele palindrom din intervalul de la 100 până la 300, care prin ridicarea la pătrat iarăși formează un număr palindrom, utilizând funcția PALINDROM. 
def PALINDROM(n):
    original=n
    invers=0
    while n>0:
        cifra=n%10
        invers=invers*10+cifra
        n=n//10
    return original==invers

numar=100
while numar<=300:
    if PALINDROM(numar):
        patrat=numar*numar
        if PALINDROM(patrat):
            print(numar)
    numar=numar+1