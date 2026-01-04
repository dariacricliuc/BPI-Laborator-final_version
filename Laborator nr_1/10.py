# Задача 10. O persoană a depus pe cont R lei. La sfârșitul fiecărei luni suma se mărește cu W procente. Ce sumă de bani va fi pe cont peste 3, 4, 5 luni?
R=float(input("Введите сумму вклада: "))
W=float(input("Введите ежемесячный процент: "))
S1=R*((1+W/100)**3)
S2=R*((1+W/100)**4)
S3=R*((1+W/100)**5)
print("Сумма через три месяца составит:", S1, "леев")
print("Сумма через четыре месяца составит:", S2, "леев")
print("Сумма через пять месяцев составит:", S3, "леев")