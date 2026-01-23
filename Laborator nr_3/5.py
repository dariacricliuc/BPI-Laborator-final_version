# Задача 5. Se introduce de la tastieră o cifră. Să se afișeze cuvântul ce descrie cifra introdusă (pentru 0 - „zero”, 1 - unu”, etc.).
cifra=int(input("Введите цифру: "))

if (cifra>=0) and (cifra<=9):
    match cifra:
        case 0: 
            print ("Ноль")
        case 1:
            print("Один")
        case 2:
            print("Два")
        case 3:
            print("Три")
        case 4:
            print("Четыре")
        case 5:
            print("Пять")
        case 6:
            print("Шесть")
        case 7:
            print("Семь")
        case 8:
            print("Восемь")
        case 9:
            print("Девять")
else:
    print("Ошибка: перепроверьте введённую цифру")