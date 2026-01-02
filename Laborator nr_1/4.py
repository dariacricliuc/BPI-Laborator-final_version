# Задача 4. Se citește un număr natural X format din exact 4 cifre nenule. Afișați numerele obținute în următoarele moduri: a) schimbând prima cifră cu ultima; b) schimbând între ele cifrele din mijloc; c) înlocuind cifrele din mijloc cu doi de 0.
x=int(input("Введите четырёхзначное натуральное число, которое не содержит нулевые цифры: "))
a=(x%10)*1000+((x//100)%10)*100+((x//10)%10)*10+(x//1000)
b=(x//1000)*1000+((x//10)%10)*100+((x//100)%10)*10+(x%10)
c=(x//1000)*1000+(x%10)
print("Первое число:", a)
print("Второе число:", b)
print("Третье число:", c)