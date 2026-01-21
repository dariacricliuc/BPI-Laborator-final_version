'''# Задача 1. Să se elaboreze un program care să citească de la tastatură trei valori numerice a, b, c şi apoi să afișeze pe ecran cea mai mare diferență dintre oricare două valori date. Exemplu: pentru a = 100, b = 15, c = 105 se va afișa 90.
a=float(input("Введите a: "))
b=float(input("Введите b: "))
c=float(input("Введите c: "))
M=max(a, b, c)
m=min(a, b, c)
d=M-m
print("Самая большая разница между тремя числами:", d)'''



'''# Задача 2. Să se elaboreze un program care să citească de la tastatură trei numere reale a, b, c și să determine dacă acestea pot constitui lungimile laturilor unui triunghi. În caz afirmativ se va afișa tipul triunghiului (oarecare, isoscel, echilateral, dreptunghic).
a=float(input("Введите a: "))
b=float(input("Введите b: "))
c=float(input("Введите c: "))

if not(a+b>c and a+c>b and b+c>a) and not(a>0 and b>0 and c>0):
    print("Треугольник не существует")  
else:
    if (a==b==c):
        print("Треугольник равносторонний")
    else:
        if a==b or b==c or a==c:
            print("Треугольник равнобедренный")
        else:
            if (a**2)+(b**2)==(c**2) or (a**2)+(c**2)==(b**2) or (b**2)+(c**2)==(a**2):
                print("Треугольник прямоугольный")
            else:
                print("Треугольник произвольный")'''
    
    
    
'''# Задача 3. Să se elaboreze un program care să citească un număr X natural din exact 3 cifre și să se genereze cel mai mare număr care are aceleași cifre ca el. Exemplu: pentru X = 192 se va afișa 921; pentru X = 364 se va afișa 643.
x=int(input("Введите целое трёхзначное число: "))
s=x//100
d=(x//10)%10
e=x%10

if s>=d and s>=e:
    if d>=e:
        m=s*100+d*10+e
    else:
        m=s*100+e*10+d
else:
    if d>=s and d>=e:
        if s>=e:
            m=d*100+s*10+e
        else:
            m=d*100+e*10+s
    else:
        if s>=d:
            m=e*100+s*10+d
        else:
            m=e*100+d*10+s
print("Самое большое число:", m)'''



'''# Задача 4. Să se elaboreze un program care să citească de la tastatură două numere reale a și b, apoi să pună utilizatorului întrebarea: Ce doriți să calculați, media aritmetică sau geometrică? Dacă se va răspunde prin 1, se va calcula și afișa media aritmetică a numerelor, iar pentru 2 – media geometrică (numai în cazul numerelor pozitive). Dacă nu se răspunde prin 1 sau 2 se va afișa ‘Răspuns incorect’.
a=float(input("Введите a: "))
b=float(input("Введите b: "))
print("Что желаете вычислить?")
print("Нажмите 1, если среднее арифметическое значение")
print("Нажмите 2, если среднее геометрическое значение")
r=int(input("Ваш ответ: "))

if r==1:
    m=(a+b)/2
    print("Среднее арифметическое значение:", m)
else:
    if r==2:
        if a>0 and b>0:
            m=(a*b)**0.5
            print("Среднее геометрическое значение:", m)
        else:
            print("Ошибка: отрицательные значения чисел")
    else:
        print("Ответ неверный")'''
    
    
    
'''# Задача 5. Să se elaboreze un program care să citească un număr X natural din exact 3 cifre și să genereze cel mai mic număr care are aceleași cifre ca el. Exemplu: pentru X = l92 se va afişa 129; pentru X = 801 se va afişa 108.
x=int(input("Введите целое и трёхзначное число: "))
s=x//100
d=(x//10)%10
e=x%10

if s<=d and s<=e:
    if d<=e:
        m=s*100+d*10+e
    else:
        m=s*100+e*10+d
else:
    if d<=s and d<=e:
        if s<=e:
            m=d*100+s*10+e
        else:
            m=d*100+e*10+s
    else:
        if s<=d:
            m=e*100+s*10+d
        else:
            m=e*100+d*10+s
print("Самое маленькое число:", m)'''



'''# Задача 6. Să se elaboreze un program care să citească data curentă (zi, lună, an) și să determine data zilei următoare.
d=int(input("Введите день: "))
m=int(input("Введите месяц: "))
g=int(input("Введите год: "))

match m:
    case 1|3|5|7|8|10|12:
        total=31
    case 4|6|9|11:
        total=30
    case 2:
        if g%4==0:
            total=29
        else:
            total=28
    case _:
        print("Неверно введённый месяц")
        exit()

d=d+1
if d>total:
    d=1
    m=m+1
    if m>12:
        m=1
        g=g+1
print("Дата следующего дня:", d, m, g)'''



'''# Задача 7. Fie a, b, c, d numere întregi citite de la tastatură. Să se elaboreze un program care să calculeze suma primelor două dacă c<d, produsul lor dacă c>d și suma inverselor, dacă c=d.
a=int(input("Введите a: "))
b=int(input("Введите b: "))
c=int(input("Введите с: "))
d=int(input("Введите d: "))

if c<d:
    r=a+b
    print("Сумма первых двух чисел:", r)
else:
    if c>d:
        r=a*b
        print("Произведение первых двух чисел:", r)
        
if a!=0 and b!=0:
    r=1/a+1/b
    print("Сумма первых двух обратных чисел:", r)
else:
    print("Ошибка: деление на ноль")'''
        
        
        
'''# Задача 8. Să se elaboreze un program care să citească un număr X natural din exact 3 cifre și să determine: dacă suma cifrelor numărului X reprezintă un număr din exact 2 cifre; dacă produsul cifrelor numărului X reprezintă un număr din exact 3 cifre; dacă produsul cifrelor numărului X este mai mare decât însuși numărul X; dacă suma cifrelor numărului X este divizibilă cu numărul Y.
X=int(input("Введите натуральное трёхзначное число: "))
Y=int(input("Введите число Y: "))
s=X//100
d=(X//10)%10
e=X%10
suma=s+d+e
pr=s*d*e

if 10<=suma<=99:
    print("Сумма цифр является двухзначным числом")
else:
    print("Сумма цифр не является двухзначным числом")
    
if 100<=pr<=999:
    print("Произведение цифр является трёхзначным числом")
else:
    print("Произведение цифр не является трёхзначным числом")

if pr>X:
    print("Произведение цифр больше самого числа Х")
else:
    print("Произведение цифр меньше самого числа Х")

if Y!=0:
    if suma%Y==0:
        print("Сумма цифр кратна числу", Y)
    else:
        print("Сумма цифр не кратна числу", Y)
else:
    print("Ошибка: деление на ноль")'''
    
    
    
'''# Задача 9. Scrieți un program care determină și afișează valoarea funcției pentru un număr real X citit de la tastatură: 𝑓(𝑥)={𝑥^2+1, 𝑥<−3; 𝑥−2, 3≤𝑥≤3; 2𝑥^2−5𝑥+1, 𝑥>3.
x=float(input("Введите x: "))

if x<-3:
    f=x**2+1
else:
    if -3<=x<=3:
        f=x-2
    else:
        f=2*x**2-5*x+1
print("Значение х по функции:", f)'''



'''# Задача 10. Orice sumă de bani S (S>7) poate fi plătită numai cu monede de 3 şi 5 lei. Dat fiind S>7, scrieți un program care să determine o modalitate de plată a sumei S numai cu monede de 3 şi 5 lei.
S=int(input("Введите сумму S: "))

if S>7:
    if S%5==0:
        print(S//5, "монет по 5 лей и 0 монет по 3 лея")
    else:
        if S%5==3:
            print(S//5, "монет по 5 лей и 1 монета по 3 лея")
        else:
            if S%5==1:
                print((S//5)-1, "монет по 5 лей и 2 монеты по 3 лея")
            else:
                if S%5==4:
                    print((S//5)-2, "монет по 5 лей и 3 монеты по 3 лея")
                else:
                    if S%5==2:
                        print((S//5)-3, "монет по 5 лей и 4 монеты по 3 лея")
else:
    print("Сумма должна быть больше 7")'''
    
    
    
'''# Задача 11. Ionel are înălțimea H1 cm, Gigel are H2 cm, iar Danuţ are H3 cm. Scrieți un program care să afișeze numele celor 3 copii în ordinea crescătoare a înălțimii.
H1=int(input("Введите рост Ionel: "))
H2=int(input("Введите рост Gigel: "))
H3=int(input("Введите рост Danuț: "))

if H1<=H2 and H1<=H3:
    if H2<=H3:
        print("Ionel, Gigel, Danuț")
    else:
        print("Ionel, Danuț, Gigel")
else:
    if H2<=H1 and H2<=H3:
        if H1<=H3:
            print("Gigel, Ionel, Danuț")
        else:
            print("Gigel, Danuț, Ionel")
    else:
        if H1<=H2:
            print("Danuț, Ionel, Gigel")
        else:
            print("Danuț, Gigel, Ionel")'''
        
        
        
'''# Задача 12. Să se elaboreze un program care să citească de la tastatură patru numere întregi distincte și să determine care dintre ele este minim și maxim.
a=int(input("Введите а: "))
b=int(input("Введите b: "))
c=int(input("Введите с: "))
d=int(input("Введите d: "))

m=a
if b<m:
    m=b
else:
    if c<m:
        m=c
    else:
        if d<m:
            m=d
            
M=a
if b>M:
    M=b
else:
    if c>M:
        M=c
    else:
        if d>M:
            M=d
print("Минимальное число:", m)
print("Максимальное число:", M)'''



'''# Задача 13. Alina are n pungulițe cu semințe a câte 20 g, ea dorește să-și facă o grădinuță de m straturi de nr metri fiecare. Știind că pentru fiecare metru semănat trebuie S grame de semințe, determinați dacă îi ajung Alinei semințe pentru întreaga grădină. 
n=int(input("Введите число мешков: "))
m=int(input("Введите число слоёв: "))
nr=float(input("Введите длину каждого слоя: "))
S=float(input("Введите количество необходимых семян: "))
total=n*20
necesar=m*nr*S

if total>=necesar:
    print("Семян достаточно для всего огорода")
else:
    print("Семян не достаточно для всего огорода")'''
    
    
    
'''# Задача 14. Să se elaboreze un program care determină soluțiile ecuației Ax^2+Bx+C=0, unde A, B, C sunt numere reale.
A=float(input("Введите A: "))
B=float(input("Введите B: "))
C=float(input("Введите C: "))

if A==0:
    if B!=0:
        x=-C/B
        print("Уравнение первой степени, результат:", x)
    else:
        if C==0:
            print("Уравнение имеет бесконечное множество решений")
        else:
            print("Уравнение не имеет решений")
else:
    delta=B**2-4*A*C
    if delta>0:
        x1=(-B+(delta)**0,5)/(2*A)
        x2=(-B-(delta)**0,5)/(2*A)
        print("Уравнение имеет два решения:", x1, "и", x2)
    else:
        if delta==0:
            x=-B/(2*A)
            print("Уравнение имеет одно решение:", x)
        else:
            print("Уравнение не имеет решений")'''
        
        
        
'''# Задача 15. Să se elaboreze un program care să citească de la tastatură două numere întregi, să verifice dacă primul număr este predecesorul celui de al doilea număr și să afișeze mesaje corespunzătoare. Exemplu: pentru 3 5 se va afișa “primul numar nu este predecesorul celui de al doilea”; pentru 5 6 se va afișa “primul numar este predecesorul celui de al doilea”.
a=int(input("Введите а: "))
b=int(input("Введите b: "))

if a+1==b:
    print("Число a предшествует числу b")
else:
    print("Число a не предшествует числу b")'''
    
    
    
'''# Задача 16. În planul cartezian xOy, se dă un dreptunghi prin colțurile stânga-jos (xs, ys) și dreapta-sus (xd, yd). Să se determine dacă un punct oarecare (x,y) se află sau nu în interiorul dreptunghiului.
xs=float(input("Введите xs: "))
ys=float(input("Введите ys: "))
xd=float(input("Введите xd: "))
yd=float(input("Введите yd: "))
x=float(input("Введите координаты х: "))
y=float(input("Введите координаты у: "))

if (xs<=x<=xd) and (ys<=y<=yd):
    print("Точка находится внутри прямоугольника")
else:
    print("Точка не находится внутри прямоугольника")'''
    
    
    
'''# Задача 17. Se citesc două intervale de timp exprimate în ore, minute şi secunde (h1,m1,s1) şi (h2,m2,s2). Să se calculeze suma celor 2 intervale de timp.
h1=int(input("Введите часы первого интервала: "))
m1=int(input("Введите минуты первого интервала: "))
s1=int(input("Введите секунды первого интервала: "))
h2=int(input("Введите часы второго интервала: "))
m2=int(input("Введите минуты второго интервала: "))
s2=int(input("Введите секунды второго интервала: "))
s=s1+s2
m=m1+m2
h=h1+h2

if s>=60:
    s=s-60
    m=m+1
if m>=60:
    m=m-60
    h=h+1
print("Новое время:", h, m, s)'''