# Задача 6. Unitățile de măsură a lungimii se numerotează în felul următor: 1 - dm, 2 - km, 3 - m, 4 - mm, 5 - cm. Se introduce lungimea segmentului și numărul unității de măsură. Să se afișeze lungimea segmentului în metri.
lungime=float(input("Введите длину: "))
unitate=int(input("Введите единицу измерения (1-дм, 2-км, 3-м, 4-мм, 5-см): "))

match unitate:
    case 1:
        metri=lungime/10
    case 2:
        metri=lungime*1000
    case 3:
        metri=lungime
    case 4:
        metri=lungime/1000
    case 5:
        metri=lungime/100
    case _:
        print("Неизвестная единица измерения")
        metri=None

if metri is not None:
    print("Длина в метрах: ", metri)