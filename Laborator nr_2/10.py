# Задача 10. Orice sumă de bani S (S>7) poate fi plătită numai cu monede de 3 şi 5 lei. Dat fiind S>7, scrieți un program care să determine o modalitate de plată a sumei S numai cu monede de 3 şi 5 lei.
S=int(input("Введите сумму S: "))

if S>7:
    if S%5==0:
        print(S//5, "монет по 5 лей и 0 монет по 3 лея")
    else:
        if S%5==3:
            print(S//5, "монет по 5 лей и 1 монета по 3 лея")
        else:
            if S%5==1:
                print((S//5)-1, "монет по 5 лей и 2 монеты по 3 лея")
            else:
                if S%5==4:
                    print((S//5)-2, "монет по 5 лей и 3 монеты по 3 лея")
                else:
                    if S%5==2:
                        print((S//5)-3, "монет по 5 лей и 4 монеты по 3 лея")
else:
    print("Сумма должна быть больше 7")