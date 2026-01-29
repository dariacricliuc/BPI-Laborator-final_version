# Задача 10. Să se elaboreze un program care verifică dacă un număr natural nenul dat este „perfect”, adică este egal cu suma divizorilor săi proprii, inclusiv 1. Exemplu: 6=1+2+3 este număr perfect.
n=int(input("Введите число: "))

suma_divizori=0
i=1
while i<n:
    if n%i==0:
        suma_divizori=suma_divizori+i
    i=i+1
if suma_divizori==n:
    print(n, "- идеальное число")
else:
    print(n, "- не идеальное число")