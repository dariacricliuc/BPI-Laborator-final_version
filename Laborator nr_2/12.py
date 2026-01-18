# Задача 12. Să se elaboreze un program care să citească de la tastatură patru numere întregi distincte și să determine care dintre ele este minim și maxim.
a=int(input("Введите а: "))
b=int(input("Введите b: "))
c=int(input("Введите с: "))
d=int(input("Введите d: "))

m=a
if b<m:
    m=b
else:
    if c<m:
        m=c
    else:
        if d<m:
            m=d
            
M=a
if b>M:
    M=b
else:
    if c>M:
        M=c
    else:
        if d>M:
            M=d
print("Минимальное число:", m)
print("Максимальное число:", M)