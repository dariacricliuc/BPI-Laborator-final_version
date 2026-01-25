# Задача 14. De la tastieră se introduce numărul caracteristicii a unui triunghi dreptunghic isoscel dintre (1–cateta (a); 2–ipotenuza (c); 3-înălțimea dusă pe ipotenuză (h); 4-aria (s)) și valoarea acesteia. Să se afișeze valorile celorlalte caracteristici.
n=int(input("Введите одну из четырёх характеристик равнобедренного и прямоугольного треугольника (1-катет; 2-гипотенуза; 3-высота, опущенная на гипотенузу; 4-площадь треугольника): "))
x=float(input("Введите значение характеристики: "))

if ((n<1) or (n>4)) or x<0:
    print("Ошибка: неверный номер характеристики или отрицательное значение характеристики")
else:
    match n:
        case 1:
            a=x
            c=((a**2)+(a**2))**0.5
            h=((a**2)-(c/2)**2)**0.5
            s=(a*a)/2
        case 2:
            c=x
            a=c/(2**0.5)
            h=((a**2)-(c/2)**2)**0.5
            s=(a*a)/2
        case 3:
            h=x
            a=h*(2**0.5)
            c=((a**2)+(a**2))**0.5
            s=(a*a)/2
        case 4:
            s=x
            a=(2*s)**0.5
            c=((a**2)+(a**2))**0.5
            h=((a**2)-(c/2)**2)**0.5
            
print("Катет a:", a)
print("Гипотенуза c:", c)
print("Высота h:", h)
print("Площадь s:", s)