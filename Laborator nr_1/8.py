# Задача 8. Se cunoaște viteza de deplasare a Valentinei către Marina – V1 km/h, și viteza de deplasare a Marinei către Valentina – V2 km/h. Să se determine peste cât timp ele se vor întâlni, dacă distanța inițială dintre ele este de S km.
v1=float(input("Введите скорость движения Валентины: "))
v2=float(input("Введите скорость движения Марины: "))
S=float(input("Введите расстояние: "))
if v1>0 and v2>0 and S>0:
    t=S/(v1+v2)
    print("Время, через которое встретятся девочки:", t, "часов")
else:
    print("Ошибка: перепроверьте введённые значения")