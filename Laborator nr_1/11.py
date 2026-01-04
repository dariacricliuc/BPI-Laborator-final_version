# Задача 11. Pe parcursul lecțiilor de informatică 4 elevi au rezolvat probleme la calculator. Primul elev a rezolvat toate problemele în N min, toți ceilalți au folosit cu 10 min mai mult decât precedentul său. Cât timp a fost necesar elevilor?
N=int(input("Введите время, за которое первый ученик решил все задачи: "))

if N>0:
    x=N+10
    print("Второй ученик решил задачи за", x, "минут")
    y=x+10
    print("Третий ученик решил задачи за", y, "минут")
    z=y+10
    print("Четвёртый ученик решил задачи за", z, "минут")
else:
    print("Ошибка: введённое значение времени неверное")