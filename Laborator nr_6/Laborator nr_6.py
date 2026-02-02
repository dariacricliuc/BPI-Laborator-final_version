'''# Задача 4. Să se elaboreze o procedură care determină aria și perimetrul unui dreptunghi determinat de laturile p și q care se introduc de la tastieră.
def dreptunghi(p, q):
    aria=p*q
    perimetru=2*(p+q)
    return aria, perimetru

p=float(input("Введите сторону p: "))
q=float(input("Введите сторону q: "))

aria, perimetru=dreptunghi(p, q)
print("Площадь прямоугольника:", aria)
print("Периметр прямоугольника:", perimetru)'''



'''# Задача 5. Să se elaboreze o procedură care calculează aria și perimetrul circumferinței de raza r care este introdusă de la tastieră.
def cerc(r):
    aria=r*3.14*r
    perimetru=2*3.14*r
    return aria, perimetru
    
r=float(input("Введите радиус окружности: ")) 
  
aria, perimetru=cerc(r)    
print("Площадь окружности:", aria)
print("Периметр окружности:", perimetru)'''



'''# Задача 6. Să se elaboreze o procedură care formează imaginea inversă a unui număr natural.
def invers(x):
    inversat=0
    while x>0:
        c=x%10
        inversat=inversat*10+c
        x=x//10
    return inversat
    
x=int(input("Введите натуральное число x: ")) 

inversat=invers(x) 
print("Обратное число:", inversat)'''