# Задача 13. Alina are n pungulițe cu semințe a câte 20 g, ea dorește să-și facă o grădinuță de m straturi de nr metri fiecare. Știind că pentru fiecare metru semănat trebuie S grame de semințe, determinați dacă îi ajung Alinei semințe pentru întreaga grădină. 
n=int(input("Введите число мешков: "))
m=int(input("Введите число слоёв: "))
nr=float(input("Введите длину каждого слоя: "))
S=float(input("Введите количество необходимых семян: "))
total=n*20
necesar=m*nr*S

if total>=necesar:
    print("Семян достаточно для всего огорода")
else:
    print("Семян не достаточно для всего огорода")