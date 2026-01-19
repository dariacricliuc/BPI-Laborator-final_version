# Задача 15. Să se elaboreze un program care să citească de la tastatură două numere întregi, să verifice dacă primul număr este predecesorul celui de al doilea număr și să afișeze mesaje corespunzătoare. Exemplu: pentru 3 5 se va afișa “primul numar nu este predecesorul celui de al doilea”; pentru 5 6 se va afișa “primul numar este predecesorul celui de al doilea”.
a=int(input("Введите a: "))
b=int(input("Введите b: "))

if a+1==b:
    print("Число a предшествует числу b")
else:
    print("Число a не предшествует числу b")