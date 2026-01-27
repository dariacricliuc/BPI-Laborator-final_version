# Задача 1. Să se elaboreze un program care calculează suma S=2+4+6+...+n, pentru n citit de la tastatură și afișează rezultatul sumei pe ecran.
n=int(input("Введите число n: "))

suma=0
i=2
while i<=n:
    suma=suma+i
    i=i+2
print("Сумма:", suma)