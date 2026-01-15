'''# Задача 1. Să se scrie un program care citește un număr de ani și calculează numărul de luni, zile și ore corespunzătoare. Se consideră că un an are 365 zile. Exemplu: Date de intrare: 2. Date de ieșire: 24 luni 730 zile 17520 ore.
y=int(input("Введите количество лет: "))

if y>=0:
    m=y*12
    d=y*365
    h=d*24
    print('Количество лет: ', y)
    print('Количество месяцев: ', m)
    print('Количество дней: ', d)
    print('Количество часов: ', h)
else:
    print("Ошибка: количество лет не может быть отрицательным числом")'''



'''# Задача 2. Se citește un număr X format din exact 4 cifre. Să se afișeze numărul care se obține prin eliminarea cifrelor din mijloc.
x=int(input("Введите четырёхзначное натуральное число: "))
y=(x//1000)*10+(x%10)
print("Новое число:", y)'''



'''# Задача 3. Ion și Vasile joacă următorul joc: Ion spune un număr, iar Vasile trebuie să găsească cinci numere consecutive, crescătoare, numărul din mijloc fiind cel ales de Ion. Ajutați-l pe Vasile să găsească răspunsul mai repede. Exemplu: Ion spune 10, Vasile spune 8 9 10 11 12.
x=int(input("Назовите любое целое число: "))
z=x-2
y=x-1
a=x+1
b=x+2
print("Последовательность чисел следующая:", z, ",", y, ",", x, ",", a, ",", b)'''



'''# Задача 4. Se citește un număr natural X format din exact 4 cifre nenule. Afișați numerele obținute în următoarele moduri: a) schimbând prima cifră cu ultima; b) schimbând între ele cifrele din mijloc; c) înlocuind cifrele din mijloc cu doi de 0.
x=int(input("Введите четырёхзначное натуральное число, которое не содержит нулевые цифры: "))
a=(x%10)*1000+((x//100)%10)*100+((x//10)%10)*10+(x//1000)
b=(x//1000)*1000+((x//10)%10)*100+((x//100)%10)*10+(x%10)
c=(x//1000)*1000+(x%10)
print("Первое число:", a)
print("Второе число:", b)
print("Третье число:", c)'''



'''# Задача 5. Se citește un număr natural X format din 4 cifre. Să se afișeze numărul obținut din suma numerelor care se obțin eliminând pe rând prima cifră a lui X, apoi primele două, apoi primele trei. Exemplu: Dacă X=2347 se obține 347+47+7=401.
x=int(input("Введите четырёхзначное натуральное число: "))
s=x%1000+x%100+x%10
print(x%1000, "+", x%100, "+", x%10, "=", s)'''



'''# Задача 6. Se cunoaște vârsta lui Nicolae – X ani și al lui Mihai – Z ani. Să se calculeze vârsta medie a acestora și diferența lor de vârstă.
x=int(input("Возраст Николая: "))
z=int(input("Возраст Михая: "))
avg=(x+z)/2
print("Средний возраст мальчиков: ", avg)

if x>z:
    print("Николай старше Михая")
    r=x-z
    print("Разница в возрасте мальчиков составляет:", r, "лет")
else:
    if z>x:
        print("Михай старше Николая")
        r=z-x
        print("Разница в возрасте мальчиков составляет:", r, "лет")
    else:
        if x==z:
            print("Мальчики являются ровесниками")'''
        
        

'''# Задача 7. Alexandra a economisit S lei și vrea să depoziteze această sumă la o bancă cu o dobânda de P% pe an, pe un termen de 3 luni. Să se afișeze dobânda obținută de Alexandra după 3 luni. Valorile S și P sunt numere naturale citite de la tastatură.
S=int(input("Введите сумму сэкономленных Александрой леев: "))
P=int(input("Введите годовой процент: "))
x=(S*P)/400
print("Сумма процентов за три месяца составляет:", x, "леев")'''      
        
        

'''# Задача 8. Se cunoaște viteza de deplasare a Valentinei către Marina – V1 km/h, și viteza de deplasare a Marinei către Valentina – V2 km/h. Să se determine peste cât timp ele se vor întâlni, dacă distanța inițială dintre ele este de S km.
v1=float(input("Введите скорость движения Валентины: "))
v2=float(input("Введите скорость движения Марины: "))
S=float(input("Введите расстояние: "))
if v1>0 and v2>0 and S>0:
    t=S/(v1+v2)
    print("Время, через которое встретятся девочки:", t, "часов")  
else:
    print("Ошибка: перепроверьте введённые значения")'''
 
 
 
'''# Задача 9. Este dat un număr real S – aria pătratului. Să se elaboreze un program care calculează latura și perimetrul acestuia.
S=float(input("Введите значение площади квадрата: "))

if S<=0:
    print("Ошибка: неверное значение площади квадрата")
else:
    a=S**(0.5)
    P=a*4 
    print("Значение стороны квадрата:", a) 
    print("Значение периметра квадрата:", P)'''



'''# Задача 10. O persoană a depus pe cont R lei. La sfârșitul fiecărei luni suma se mărește cu W procente. Ce sumă de bani va fi pe cont peste 3, 4, 5 luni?
R=float(input("Введите сумму вклада: "))
W=float(input("Введите ежемесячный процент: "))
S1=R*((1+W/100)**3)
S2=R*((1+W/100)**4)
S3=R*((1+W/100)**5)
print("Сумма через три месяца составит:", S1, "леев")
print("Сумма через четыре месяца составит:", S2, "леев")
print("Сумма через пять месяцев составит:", S3, "леев")'''



'''# Задача 11. Pe parcursul lecțiilor de informatică 4 elevi au rezolvat probleme la calculator. Primul elev a rezolvat toate problemele în N min, toți ceilalți au folosit cu 10 min mai mult decât precedentul său. Cât timp a fost necesar elevilor?
N=int(input("Введите время, за которое первый ученик решил все задачи: "))

if N>0:
    x=N+10
    print("Второй ученик решил задачи за", x, "минут")
    y=x+10
    print("Третий ученик решил задачи за", y, "минут")
    z=y+10
    print("Четвёртый ученик решил задачи за", z, "минут")
else:
    print("Ошибка: введённое значение времени неверное")'''
    
    
    
'''# Задача 12. Este dat un număr natural N. Să se elaboreze un program care calculează câte ore, minute, secunde sunt în N zile (o zi = 24 ore).
N=int(input("Введите количество дней: "))

if N>=0:
    h=N*24
    m=h*60
    s=m*60
    print("Количество дней:", N)
    print("Количество часов:", h)
    print("Количество минут:", m)
    print("Количество секунд:", s) 
else:
    print("Ошибка: количество дней не может быть отрицательным числом")'''



'''# Задача 13. Elevul dorește să înscrie pe o dischetă 3 fișiere de dimensiuni X, Y, Z Kb. Volumul dischetei este de 1,41Mb. De câte dischete are nevoie elevul?
print("Объём диска равен 1,41Mb")
x=float(input("Введите размер первого файла: "))
y=float(input("Введите размер второго файла: "))
z=float(input("Введите размер третьего файла: "))
d=1410
s=x+y+z
n=s//d

if n>0:
    print("Всего необходимо:", n, "дисков") 
else:
    if n==0:
        print("Новые диски не нужны")
    else:
        print("Ошибка: количество дисков не может быть отрицательным числом")'''
        


'''# Задача 14. Se citește un număr natural X format din 4 cifre. Să se afișeze numărul obținut din suma numerelor care se obțin eliminând pe rând ultima cifră a lui X, apoi ultimele două, apoi ultimele trei. Exemplu. Dacă X=2347 se obține 234+23+2=259.
x=int(input("Введите четырёхзначное натуральное число: "))
s=x//10+x//100+x//1000
print(x//10, "+", x//100, "+", x//1000, "=", s)'''



'''# Задача 15. O familie a hotărât să schimbe vechiul său automobil pe unul nou. Prețul cu care poate fi vândut automobilul vechi este N lei, suma de pe contul bancar al familiei este de K lei. Luând în considerație că suma de care dispune familia este mai mare decât prețul automobilului nou și prețul acestuia este de X lei, să se determine ce sumă de bani va avea familia după procurarea automobilului.
N=float(input("Введите цену старого автомобиля: "))
K=float(input("Введите сумму на счету: "))
X=float(input("Введите цену нового автомобиля: "))

if (N>0) and (K>0) and (X>0):
    S=(K+N)-X
    print("Оставшаяся сумма на счету равна", S, "леев")
else:
    print("Ошибка: перепроверьте введённые значения")'''



'''# Задача 16. Să se afișeze imaginea inversă a numărul natural introdus de 3 cifre.
x=int(input("Введите трёхзначное натуральное число: "))
s=(x%10)*100+((x%100)//10)*10+(x//100)
print("Обратное число:", s)'''



'''# Задача 17. # Задача 17. Se cunoaște ora începerii lecțiilor la școală: N ore și M minute. Durata fiecărei lecții este 45 min., prima și a treia recreație durează 15 min., iar celelalte 10 min. Să se afișeze ora finisării lecției a 7-a.
N=int(input("Назовите часы начала уроков: "))
M=int(input("Назовите минуты начала уроков: "))
T=7*45+15+10+15+10+10+10
min=M+(T%60)
H=N+(T//60)

if min>=60:
    H=H+1
    min=min-60
    
if N>0 and M>0:
    print("Время окончания седьмого урока:", H, ":", min)
else:
    print("Ошибка: отрицательное значение времени")'''