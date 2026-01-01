# Задача 3. Ion și Vasile joacă următorul joc: Ion spune un număr, iar Vasile trebuie să găsească cinci numere consecutive, crescătoare, numărul din mijloc fiind cel ales de Ion. Ajutați-l pe Vasile să găsească răspunsul mai repede. Exemplu: Ion spune 10, Vasile spune 8 9 10 11 12. 
x=int(input("Назовите любое целое число: "))
z=x-2
y=x-1
a=x+1
b=x+2
print("Последовательность чисел следующая:", z, ",", y, ",", x, ",", a, ",", b)