# Задача 4. Se citește un text cu cel mult 255 de caractere. Scrieți un program care afișează: vocalele din text și numărul lor; exemplu: bacalaureat - aaauea 6; consoanele și numărul lor; exemplu: bacalaureat - bclrt 5. 
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
print("Согласные:", consoane_gasite, numar_consoane)