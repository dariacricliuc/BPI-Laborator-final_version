# Задача 9. Este dat un număr real S – aria pătratului. Să se elaboreze un program care calculează latura și perimetrul acestuia.
S=float(input("Введите значение площади квадрата: "))

if S<=0:
    print("Ошибка: неверное значение площади квадрата")
else:
    a=S**(0.5)
    P=a*4 
    print("Значение стороны квадрата:", a) 
    print("Значение периметра квадрата:", P)