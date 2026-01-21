# Задача 1. De la tastieră se introduce un caracter ch. Să se precizeze și afișeze felul caracterului (literă, cifră, operator). În caz dacă nu este nici unul din cele enumerate, să se afișeze „Caracter necunoscut”.
ch=input("Введите один символ: ")

match ch:
    case 'a'|'b'|'c'|'d'|'e'|'f'|'g'|'h'|'i'|'j'|'k'|'l'|'m'|'n'|'o'|'p'|'q'|'r'|'s'|'t'|'u'|'v'|'w'|'x'|'y'|'z'|'A'|'B'|'C'|'D'|'E'|'F'|'G'|'H'|'I'|'J'|'K'|'L'|'M'|'N'|'O'|'P'|'Q'|'R'|'S'|'T'|'U'|'V'|'W'|'X'|'Y'|'Z':
        print("Буква")
    case '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9':
        print("Цифра")
    case '+'|'-'|'*'|'/':
        print("Оператор")
    case _:
        print("Неизвестный символ")