# Задача 11. Se cunosc lungimea şi lăţimea unei suprafeţe în formă dreptunghiulară. Să se elaboreze un program care realizează un meniu în care atunci când se va tasta 1 să se afişeze perimetrul suprafeţei, când se tastează 2 să se afişeze aria, iar când se tastează 3 să se afișeze diagonala suprafeței. Se va verifica şi corectitudinea introducerii datelor.
lungime=float(input("Введите длину: "))
latime=float(input("Введите ширину: "))
optiune=int(input("Выберите опцию (1-периметр, 2-площадь, 3-диагональ): "))

match optiune:
    case 1:
        perimetru=2*(lungime+latime)
        print("Периметр:", perimetru)
    case 2:
        arie=lungime*latime
        print("Площадь:", arie)
    case 3:
        diagonala=(lungime**2+latime**2)**0.5
        print("Диагональ:", diagonala)
    case _:
        print("Неизвестная опция")