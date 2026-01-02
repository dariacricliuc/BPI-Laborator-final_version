# Задача 6. Se cunoaște vârsta lui Nicolae – X ani și al lui Mihai – Z ani. Să se calculeze vârsta medie a acestora și diferența lor de vârstă.
x=int(input("Возраст Николая: "))
z=int(input("Возраст Михая: "))
avg=(x+z)/2
print("Средний возраст мальчиков: ", avg)

if x>z:
    print("Николай старше Михая")
    r=x-z
    print("Разница в возрасте мальчиков составляет:", r, "лет")
else:
    if z>x:
        print("Михай старше Николая")
        r=z-x
        print("Разница в возрасте мальчиков составляет:", r, "лет")
    else:
        if x==z:
            print("Мальчики являются ровесниками")