# Задача 17. O persoană a deschis un cont în bancă în sumă de 1000 lei. Venitul la sfârșitul fiecărei luni face 2%. De determinat ce sumă va fi pe cont după 6 luni.
suma=1000
luna=1
while luna<=6:
    suma=suma+suma*0.02
    luna=luna+1
print("Сумма после шести месяцев:", suma)