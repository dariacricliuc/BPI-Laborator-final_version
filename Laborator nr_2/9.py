# Задача 9. Scrieți un program care determină și afișează valoarea funcției pentru un număr real X citit de la tastatură: 𝑓(𝑥)={𝑥^2+1, 𝑥<−3; 𝑥−2, 3≤𝑥≤3; 2𝑥^2−5𝑥+1, 𝑥>3.
x=float(input("Введите x: "))

if x<-3:
    f=x**2+1
else:
    if -3<=x<=3:
        f=x-2
    else:
        f=2*x**2-5*x+1
print("Значение х по функции:", f)