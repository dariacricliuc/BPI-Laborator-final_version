# Задача 6. Se citește un text de cel mult 255 de caractere. Scrieți un program care verifică dacă șirul de caractere este palindrom.
text=input("Введите текст: ")

i=0
j=len(text)-1
palindrom=True
while i<j:
    if text[i]!=text[j]:
        palindrom=False
        break
    i=i+1
    j=j-1
if palindrom:
    print("Текст является палиндромом")
else:
    print("Текст не является палиндромом")