# Задача 15. Un robot se poate deplasa în 4 direcții (“N”-Nord; “S”-Sud; “V”-Vest; ”E”-Est) și poate îndeplini 3 instrucțiuni: 0-continuă deplasarea; 1-la stânga; 2-la dreapta. De la tastieră se introduce simbolul direcției inițiale a robotului și instrucțiunea ce trebuie îndeplinită. Să se afișeze direcția de deplasare a robotului după îndeplinirea instrucțiunii.
direction=input("Введите начальное направление (С, Ю, З, В): ")
instruction=int(input("Введите инструкцию (0-продолжить, 1-влево, 2-вправо): "))

if direction not in ("С", "Ю", "З", "В") or instruction not in (0, 1, 2):
    print("Ошибка: перепроверьте введённые данные")
else:
    match instruction:
        case 0:
            rezultat=direction
        case 1:
            match direction:
                case "С":
                    rezultat="З"
                case "З":
                    rezultat="Ю"
                case "Ю":
                    rezultat="В"
                case "В":
                    rezultat="С"     
        case 2:
            match direction:
                case "С":
                    rezultat="В"
                case "В":
                    rezultat="Ю"
                case "Ю":
                    rezultat="З"
                case "З":
                    rezultat="С"

print("Робот теперь движется следующим образом:", rezultat)