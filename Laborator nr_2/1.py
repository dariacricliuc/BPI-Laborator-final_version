# Задача 1. Să se elaboreze un program care să citească de la tastatură trei valori numerice a, b, c şi apoi să afișeze pe ecran cea mai mare diferență dintre oricare două valori date. Exemplu: pentru a = 100, b = 15, c = 105 se va afișa 90.
a=float(input("Введите a: "))
b=float(input("Введите b: "))
c=float(input("Введите c: "))
M=max(a, b, c)
m=min(a, b, c)
d=M-m
print("Самая большая разница между тремя числами:", d)