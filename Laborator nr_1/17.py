# Задача 17. Se cunoaște ora începerii lecțiilor la școală: N ore și M minute. Durata fiecărei lecții este 45 min., prima și a treia recreație durează 15 min., iar celelalte 10 min. Să se afișeze ora finisării lecției a 7-a. 
N=int(input("Назовите часы начала уроков: "))
M=int(input("Назовите минуты начала уроков: "))
T=7*45+15+10+15+10+10+10
min=M+(T%60)
H=N+(T//60)

if min>=60:
    H=H+1
    min=min-60

if N>0 and M>0:
    print("Время окончания седьмого урока:", H, ":", min)
else:
    print("Ошибка: отрицательное значение времени")