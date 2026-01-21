# Задача 17. Se citesc două intervale de timp exprimate în ore, minute şi secunde (h1,m1,s1) şi (h2,m2,s2). Să se calculeze suma celor 2 intervale de timp.
h1=int(input("Введите часы первого интервала: "))
m1=int(input("Введите минуты первого интервала: "))
s1=int(input("Введите секунды первого интервала: "))
h2=int(input("Введите часы второго интервала: "))
m2=int(input("Введите минуты второго интервала: "))
s2=int(input("Введите секунды второго интервала: "))
s=s1+s2
m=m1+m2
h=h1+h2

if s>=60:
    s=s-60
    m=m+1
if m>=60:
    m=m-60
    h=h+1
print("Новое время:", h, m, s)