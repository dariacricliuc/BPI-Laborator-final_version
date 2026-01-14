# Задача 15. O familie a hotărât să schimbe vechiul său automobil pe unul nou. Prețul cu care poate fi vândut automobilul vechi este N lei, suma de pe contul bancar al familiei este de K lei. Luând în considerație că suma de care dispune familia este mai mare decât prețul automobilului nou și prețul acestuia este de X lei, să se determine ce sumă de bani va avea familia după procurarea automobilului.
N=float(input("Введите цену старого автомобиля: "))
K=float(input("Введите сумму на счету: "))
X=float(input("Введите цену нового автомобиля: "))

if (N>0) and (K>0) and (X>0):
    S=(K+N)-X
    print("Оставшаяся сумма на счету равна", S, "леев")
else:
    print("Ошибка: перепроверьте введённые значения")