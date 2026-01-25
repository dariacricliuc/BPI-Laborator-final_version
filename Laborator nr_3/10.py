# Задача 10. Se introduce un număr din intervalul 1..10 care reprezintă nota la purtare a elevului. Să se afișeze caracterizarea verbală a notei (1..4-nesatisfăcătoare; 5, 6-satisfăcătoare; 7, 8-bună; 9, 10-exemplară).
nota=int(input("Введите оценку (1-10): "))

match nota:
    case 1|2|3|4:
        print("Неудовлетворительно")
    case 5|6:
        print("Удовлетворительно")
    case 7|8:
        print("Хорошо")
    case 9|10:
        print("Очень хорошо")
    case _:
        print("Неизвестная оценка")