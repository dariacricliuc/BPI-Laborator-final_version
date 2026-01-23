# Задача 7. Se introduce de la tastieră un număr întreg din diapazonul 100..999. Să se afișeze un șir de caractere care descrie verbal numărul, de exemplu: 250 - „două sute cincizeci”.
num=int(input("Введите натуральное и трёхзначное число из интервала от 100 до 999: "))

if (num>=100) and (num<=999):
    c_1=num//100
    c_2=(num//10)%10
    c_3=num%10
    print("Полученный результат: ", end="") 
    match c_1:
        case 1: 
            print("Сто", end="")
        case 2:
            print("Двести", end="")
        case 3:
            print("Триста", end="")
        case 4:
            print("Четыреста", end="")
        case 5:
            print("Пятьсот", end="")
        case 6:
            print("Шестьсот", end="")
        case 7:
            print("Семьсот", end="")
        case 8:
            print("Восемьсот", end="")
        case 9:
            print("Девятьсот", end="")    
    if c_2 == 1:
        match c_3:  
            case 0: 
                print(" десять", end="")
            case 1:
                print(" одинадцать", end="")
            case 2:
                print(" двенадцать", end="")
            case 3:
                print(" тринадцать", end="")
            case 4:
                print(" четырнадцать", end="")
            case 5:
                print(" пятнадцать", end="")
            case 6:
                print(" шестнадцать", end="")
            case 7:
                print(" семнадцать", end="")
            case 8:
                print(" восемнадцать", end="")
            case 9:
                print(" девятнадцать", end="")       
    else:
        match c_2:
            case 0:
                pass   
            case 2: 
                print(" двадцать", end="")
            case 3:
                print(" тридцать", end="")
            case 4:
                print(" сорок", end="")
            case 5:
                print(" пятьдесят", end="")
            case 6:
                print(" шестьдесят", end="")
            case 7:
                print(" семьдесят", end="")
            case 8:
                print(" восемьдесят", end="")
            case 9:
                print(" девяносто", end="")      
        match c_3:
            case 0:
                pass
            case 1:
                print(" один", end="")
            case 2:
                print(" два", end="")
            case 3:
                print(" три", end="")
            case 4:
                print(" четыре", end="")
            case 5:
                print(" пять", end="")
            case 6:
                print(" шесть", end="")
            case 7:
                print(" семь", end="")
            case 8:
                print(" восемь", end="")
            case 9:
                print(" девять", end="")     
else:
    print("Ошибка: перепроверьте введённое число")