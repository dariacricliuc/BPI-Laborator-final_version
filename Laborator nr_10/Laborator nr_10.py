'''# Задача 4. Se citește un text cu cel mult 255 de caractere. Scrieți un program care afișează: vocalele din text și numărul lor; exemplu: bacalaureat - aaauea 6; consoanele și numărul lor; exemplu: bacalaureat - bclrt 5. 
text=input("Введите текст: ")

vocale="aeiouAEIOU"
consoane="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vocale_gasite=""
numar_vocale=0
i=0
while i<len(text):
    if text[i] in vocale:
        vocale_gasite=vocale_gasite+text[i]
        numar_vocale=numar_vocale+1
    i=i+1
print("Гласные:", vocale_gasite, numar_vocale)

consoane_gasite=""
numar_consoane=0
i=0
while i<len(text):
    if text[i] in consoane:
        consoane_gasite=consoane_gasite+text[i]
        numar_consoane=numar_consoane+1
    i=i+1
print("Согласные:", consoane_gasite, numar_consoane)'''



'''# Задача 5. Se citește un text de cel mult 255 caractere, care se termină cu caracterul ‘.’ și un șir de caractere sc. Scrieți un program care elimină toate aparițiile șirului sc din text. Exemplu: ‘abcab dab.’ și sc=‘ab’ - ‘c d’ 
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
print("Текст без исключённой строки", sc+":", rezultat)'''



'''# Задача 6. Se citește un text de cel mult 255 de caractere. Scrieți un program care verifică dacă șirul de caractere este palindrom.
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
    print("Текст не является палиндромом")'''