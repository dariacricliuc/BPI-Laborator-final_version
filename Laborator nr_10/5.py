# Задача 5. Se citește un text de cel mult 255 caractere, care se termină cu caracterul ‘.’ și un șir de caractere sc. Scrieți un program care elimină toate aparițiile șirului sc din text. Exemplu: ‘abcab dab.’ și sc=‘ab’ - ‘c d’ 
text=input("Введите текст: ")
sc=input("Введите строку, которую необходимо исключить: ")

i=0
rezultat=""
while i<len(text):
    if text[i:i+len(sc)]==sc:
        i=i+len(sc)
    else:
        rezultat=rezultat+text[i]
        i=i+1
print("Текст без исключённой строки", sc+":", rezultat)