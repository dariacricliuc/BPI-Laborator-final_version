# Задача 9. Elementele circumferinței se numerotează în felul următor: 1-raza; 2-diametru; 3-lungimea; 4-aria. Se introduce valoarea elementului și numărul său. Să se afișeze valorile celorlalte elemente ale circumferinței.
valoare=float(input("Введите значение: "))
element=int(input("Введите элемент (1-радиус, 2-диаметр, 3-длина, 4-площадь): "))
П=3.14

match element:
    case 1:
        r=valoare
        d=2*r
        l=2*П*r
        a=П*r*r
    case 2:
        d=valoare
        r=d/2
        l=2*П*r
        a=П*r*r
    case 3:
        l=valoare
        r=l/(2*П)
        d=2*r
        a=П*r*r
    case 4:
        a=valoare
        r=(a/П)**0.5
        d=2*r
        l=2*П*r
    case _:
        print("Неизвестный элемент")
        r=d=l=a=None

if r is not None:
    print("Радиус:", r)
    print("Диаметр:", d)
    print("Длина:", l)
    print("Площадь:", a)