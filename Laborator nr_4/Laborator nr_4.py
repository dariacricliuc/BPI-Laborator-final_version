'''# Задача 1. Să se elaboreze un program care calculează suma S=2+4+6+...+n, pentru n citit de la tastatură și afișează rezultatul sumei pe ecran.
n=int(input("Введите число n: "))

suma=0
i=2
while i<=n:
    suma=suma+i
    i=i+2
print("Сумма:", suma)'''



'''# Задача 2. Se citesc numerele n și k de la tastatură și apoi n–numere naturale pe rând. Să se elaboreze un program care afișează acele numere dintre cele n introduse care au exact k divizori.
n=int(input("Введите количество чисел: "))
k=int(input("Введите количество делителей: "))

i=1
result=""
while i<=n:
    x=int(input("Введите число: "))
    divisors=0
    j=1
    while j*j<=x:
        if x%j==0:
            if j*j==x:
                divisors=divisors+1
            else:
                divisors=divisors+2
        j=j+1
    if divisors==k:
        if result=="":
            result=str(x)
        else:
            result=result+" "+str(x)
    i=i+1
    
if result=="":
    print("Нет чисел с", k, "делителями")
else:
    print("Числа с", k, "делителями:", result)'''



'''# Задача 3. Se citește un număr natural n și apoi n numere reale. Să se elaboreze un program care calculează și afișează raportul dintre suma numerelor impare și suma numerelor pare.
n=int(input("Введите количество чисел: "))

count=1
suma_impare=0
suma_pare=0
while count<=n:
    numar=float(input("Введите число: "))
    if numar%2==1:
        suma_impare=suma_impare+numar
    else:
        suma_pare=suma_pare+numar
    count=count+1
if suma_pare!=0:
    raport=suma_impare/suma_pare
    print("Отношение:", raport)
else:
    print("Отношение не вычислимо")'''



'''# Задача 4. Să se elaboreze un program care afișează numerele de două cifre care au ultima cifră divizibilă cu 3.
x=10 
while (x<=99):
    c=x%10
    if (c%3==0):
        print("Последняя цифра данного числа кратна трём")
    else:
        print("Последняя цифра данного числа не кратна трём")
    x=x+1'''



'''# Задача 5. Să se elaboreze un program care citește un șir de n numere reale și afișează valoarea minimă și cea maximă din acest șir.
n=int(input("Введите количество чисел: "))
x=float(input("Введите первое число: "))

minim=x
maxim=x
i=1
while (i<n):
    x=float(input("Введите следующее число: "))
    if x<minim:
        minim=x
    if x>maxim:
        maxim=x
    i=i+1
print("Минимальное значение:", minim)
print("Максимальное значение:", maxim)'''



'''# Задача 6. Să se elaboreze un program care afișează toate numerele de 3 cifre, suma cifrelor cărora este divizibilă prin 5.
x=100
while (x<=999):
    a=x//100          
    b=(x//10)%10   
    c=x%10
    s=a+b+c
    if (s%5==0):
        print("Сумма цифр числа кратна пяти")
    else:
        print("Сумма цифр числа не кратна пяти")
    x=x+1'''



'''# Задача 7. De la tastatură se introduc 10 numere întregi. Să se elaboreze un program care determină și afișează: numărul celor pozitive și suma lor; media aritmetică а celor negative.
count_poz=0
suma_poz=0
suma_neg=0
count_neg=0
i=1
while i<=10:
    numar=int(input("Введите целое число: "))
    if numar>0:
        count_poz=count_poz+1
        suma_poz=suma_poz+numar
    else:
        if numar<0:
            count_neg=count_neg+1
            suma_neg=suma_neg+numar
    i=i+1
print("Позитивные числа:", count_poz)
print("Сумма позитивных чисел:", suma_poz)

if count_neg>0:
    media_neg=suma_neg/count_neg
    print("Среднее значение негативных чисел:", media_neg)
else:
    print("Негативных чисел нет")'''



'''# Задача 8. Să se elaboreze un program care calculează suma S=1+1*2+1*2*3+..+1*2*..*n.
n=int(input("Введите n: "))

suma=0
produs=1
i=1
while i<=n:
    produs=produs*i
    suma=suma+produs
    i=i+1
print("Сумма:", suma)'''



'''# Задача 9. Să se elaboreze un program care calculează suma S=1–2+3–4+..+(-)n.
n=int(input("Введите n: "))

suma=0
i=1
while i<=n:
    if i%2==1:
        suma=suma+i
    else:
        suma=suma-i
    i=i+1
print("Сумма:", suma)'''



'''# Задача 10. Să se elaboreze un program care verifică dacă un număr natural nenul dat este „perfect”, adică este egal cu suma divizorilor săi proprii, inclusiv 1. Exemplu: 6=1+2+3 este număr perfect.
n=int(input("Введите число: "))

suma_divizori=0
i=1
while i<n:
    if n%i==0:
        suma_divizori=suma_divizori+i
    i=i+1
if suma_divizori==n:
    print(n, "- идеальное число")
else:
    print(n, "- не идеальное число")'''



'''# Задача 11. Să se elaboreze un program care afișează toate numerele de 3 cifre, care sunt egale cu diferența dintre pătratul numărului alcătuit din primele 2 cifre și pătratul ultimei cifre. Exemplu: Date de intrare: n=147, Date de ieşire: 14*14–7*7=147.
numar=100
while numar<=999:
    primele_doua=numar//10
    ultima=numar%10  
    diferenta=primele_doua*primele_doua-ultima*ultima
    if diferenta==numar:
        print(primele_doua, "*", primele_doua, "-", ultima, "*", ultima, "=", numar)
    numar=numar+1'''



'''# Задача 12. De realizat un program de afișare a tuturor numerelor de 2 cifre, suma cifrelor cărora este egală cu un număr dat.
n=int(input("Введите сумму цифр: "))

numar=10
while numar<=99:
    cifra1=numar//10     
    cifra2=numar%10     
    suma_cifre=cifra1+cifra2
    if suma_cifre==n:       
        print(numar)   
    numar=numar+1'''



'''# Задача 13. Să se elaboreze un program care generează toate numerele de patru cifre de forma (3a2b) care se divid cu 9.
numar=1000
while numar<=9999:
    mii=numar//1000
    sute=(numar//100)%10
    zeci=(numar//10)%10
    unitati=numar%10  
    if (mii==3) and (zeci==2) and (numar%9==0):
        print(numar)
    else:
        print("Число не соответсвует установленным правилам")
    numar=numar+1'''



'''# Задача 14. Se citesc n numere întregi, pe rând într-o variabilă x şi o valoare întreagă a. Să se elaboreze un program care determină numărul de apariții ale valorii a, printre numerele citite.
n=int(input("Введите количество чисел: "))
a=int(input("Введите значение: "))

count=0
i=1
while i<=n:
    x=int(input("Введите число: "))
    if x==a:
        count=count+1
    i=i+1
print("Значение", a, "появляется", count, "раз")'''



'''# Задача 15. Se dă un număr natural n. Să se elaboreze un program care îl descompune și afișează, dacă este posibil, ca sumă a două numere consecutive. Exemplu: Date de intrare: n=5; Date de ieşire: 5=2+3; Date de intrare: n=6; Date de ieşire: Nu e posibil.
n=int(input("Введите число n: "))

gasit=False
i=1
while i<n:
    if i+(i+1)==n:
        print(n, "=", i, "+", i+1)
        gasit=True
        break
    i=i+1
if not gasit:
    print("Невозможно")'''



'''# Задача 16. Se consideră „fericit” biletul de 6 cifre, dacă suma primelor 3 cifre a căruia este egală cu suma ultimelor 3 cifre. Să se elaboreze un program care afișează toate numerele fericite.
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
    numar=numar+1'''



'''# Задача 17. O persoană a deschis un cont în bancă în sumă de 1000 lei. Venitul la sfârșitul fiecărei luni face 2%. De determinat ce sumă va fi pe cont după 6 luni.
suma=1000
luna=1
while luna<=6:
    suma=suma+suma*0.02
    luna=luna+1
print("Сумма после шести месяцев:", suma)'''