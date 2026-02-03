'''# Задача 4. De la tastatură se introduc 3 numere reale a, b și c. Să se elaboreze un program care calculează valoarea expresiei MAX(a-b, a, a+b)+MAX(a, b+c, a-c), utilizând funcția MAX.
def MAX(x, y, z):
    if x>=y and x>=z:
        return x
    elif y>=z:
        return y
    else:
        return z

a=float(input("Введите a: "))
b=float(input("Введите b: "))
c=float(input("Введите c: "))

rezultat=MAX(a-b, a, a+b)+MAX(a, b+c, a-c)
print("Результат:", rezultat)'''



'''# Задача 5. Să se elaboreze un program care afișează toate numerele palindrom din intervalul de la 100 până la 300, care prin ridicarea la pătrat iarăși formează un număr palindrom, utilizând funcția PALINDROM. 
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
    numar=numar+1'''



'''# Задача 6. Să se elaboreze un program care afișează valorile funcției f(x)=3x^2+x+2 pe intervalul [-2; 5] cu pasul h=1, utilizând funcția definită.
def f(x):
    return 3*x*x+x+2

x=-2
while x<=5:
    y=f(x)
    print("f(", x,")=", y)
    x=x+1'''