# Задача 14. Să se elaboreze un program care determină soluțiile ecuației Ax^2+Bx+C=0, unde A, B, C sunt numere reale.
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
            print("Уравнение не имеет решений")