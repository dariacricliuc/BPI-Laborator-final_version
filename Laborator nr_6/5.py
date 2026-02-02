# Задача 5. Să se elaboreze o procedură care calculează aria și perimetrul circumferinței de raza r care este introdusă de la tastieră.
def cerc(r):
    aria=r*3.14*r
    perimetru=2*3.14*r
    return aria, perimetru
    
r=float(input("Введите радиус окружности: "))    
  
aria, perimetru=cerc(r)    
print("Площадь окружности:", aria)
print("Периметр окружности:", perimetru)