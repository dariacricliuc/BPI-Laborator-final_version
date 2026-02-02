# Задача 4. Să se elaboreze o procedură care determină aria și perimetrul unui dreptunghi determinat de laturile p și q care se introduc de la tastieră.
def dreptunghi(p, q):
    aria=p*q
    perimetru=2*(p+q)
    return aria, perimetru

p=float(input("Введите сторону p: "))
q=float(input("Введите сторону q: "))

aria, perimetru=dreptunghi(p, q)
print("Площадь прямоугольника:", aria)
print("Периметр прямоугольника:", perimetru)