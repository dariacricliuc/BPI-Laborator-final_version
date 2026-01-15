# Задача 16. Să se afișeze imaginea inversă a numărul natural introdus de 3 cifre.
x=int(input("Введите трёхзначное натуральное число: "))
s=(x%10)*100+((x%100)//10)*10+(x//100)
print("Обратное число:", s)