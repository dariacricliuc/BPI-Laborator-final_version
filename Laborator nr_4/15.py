# Задача 15. Se dă un număr natural n. Să se elaboreze un program care îl descompune și afișează, dacă este posibil, ca sumă a două numere consecutive. Exemplu: Date de intrare: n=5; Date de ieşire: 5=2+3; Date de intrare: n=6; Date de ieşire: Nu e posibil.
n=int(input("Введите число n: "))

gasit=False
i=1
while i<n:
    if i+(i+1)==n:
        print(n, "=", i, "+", i+1)
        gasit=True
        break
    i=i+1
if not gasit:
    print("Невозможно")