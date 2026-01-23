# Задача 8. Scrieți un program care să permită alegerea unei opțiuni dintr-un anumit meniu afișat pe ecran: se afișează meniul: 1-suma; 2-produs. Apoi se introduc două numere şi se alege o operație din meniu prin introducerea numărului de ordine. Pe ecran să se afișeze expresia şi valoarea calculată.
print("Меню:")
print("1-сумма")
print("2-произведение")
a=float(input("Введите первое число: "))
b=float(input("Введите второе число: "))
optiune=int(input("Выберите опцию (1 или 2): "))

match optiune:
    case 1:
        rezultat=a+b
        print("Результат (1 - сумма):", rezultat)
    case 2:
        rezultat=a*b
        print("Результат (2 - произведение):", rezultat)
    case _:
        print("Неизвестная опция")