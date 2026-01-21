# Задача 16. În planul cartezian xOy, se dă un dreptunghi prin colțurile stânga-jos (xs, ys) și dreapta-sus (xd, yd). Să se determine dacă un punct oarecare (x,y) se află sau nu în interiorul dreptunghiului.
xs=float(input("Введите xs: "))
ys=float(input("Введите ys: "))
xd=float(input("Введите xd: "))
yd=float(input("Введите yd: "))
x=float(input("Введите координаты х: "))
y=float(input("Введите координаты у: "))

if (xs<=x<=xd) and (ys<=y<=yd):
    print("Точка находится внутри прямоугольника")
else:
    print("Точка не находится внутри прямоугольника")