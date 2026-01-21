# Задача 3. Să se elaboreze un program care determină dacă caracterul citit de la tastieră este vocală sau consoană.
ch=input("Введите символ: ")

match ch:
    case 'a'|'e'|'i'|'o'|'u'|'A'|'E'|'I'|'O'|'U':
        print("Гласная")
    case 'b'|'c'|'d'|'f'|'g'|'h'|'j'|'k'|'l'|'m'|'n'|'p'|'q'|'r'|'s'|'t'|'v'|'w'|'x'|'y'|'z'|'B'|'C'|'D'|'F'|'G'|'H'|'J'|'K'|'L'|'M'|'N'|'P'|'Q'|'R'|'S'|'T'|'V'|'W'|'X'|'Y'|'Z':
        print("Согласная")
    case _:
        print("Символ не является буквой")