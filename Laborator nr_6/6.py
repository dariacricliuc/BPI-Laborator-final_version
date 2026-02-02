# Задача 6. Să se elaboreze o procedură care formează imaginea inversă a unui număr natural.
def invers(x):
    inversat=0
    while x>0:
        c=x%10
        inversat=inversat*10+c
        x=x//10
    return inversat
    
x=int(input("Введите натуральное число x: ")) 

inversat=invers(x) 
print("Обратное число:", inversat)