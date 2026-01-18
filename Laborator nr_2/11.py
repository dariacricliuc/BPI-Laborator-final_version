# Задача 11. Ionel are înălțimea H1 cm, Gigel are H2 cm, iar Danuţ are H3 cm. Scrieți un program care să afișeze numele celor 3 copii în ordinea crescătoare a înălțimii.
H1=int(input("Введите рост Ionel: "))
H2=int(input("Введите рост Gigel: "))
H3=int(input("Введите рост Danuț: "))

if H1<=H2 and H1<=H3:
    if H2<=H3:
        print("Ionel, Gigel, Danuț")
    else:
        print("Ionel, Danuț, Gigel")
else:
    if H2<=H1 and H2<=H3:
        if H1<=H3:
            print("Gigel, Ionel, Danuț")
        else:
            print("Gigel, Danuț, Ionel")
    else:
        if H1<=H2:
            print("Danuț, Ionel, Gigel")
        else:
            print("Danuț, Gigel, Ionel")