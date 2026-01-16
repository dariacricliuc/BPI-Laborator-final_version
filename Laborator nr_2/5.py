# Задача 5. Să se elaboreze un program care să citească un număr X natural din exact 3 cifre și să genereze cel mai mic număr care are aceleași cifre ca el. Exemplu: pentru X = l92 se va afişa 129; pentru X = 801 se va afişa 108.
x=int(input("Введите целое и трёхзначное число: "))
s=x//100
d=(x//10)%10
e=x%10

if s<=d and s<=e:
    if d<=e:
        m=s*100+d*10+e
    else:
        m=s*100+e*10+d
else:
    if d<=s and d<=e:
        if s<=e:
            m=d*100+s*10+e
        else:
            m=d*100+e*10+s
    else:
        if s<=d:
            m=e*100+s*10+d
        else:
            m=e*100+d*10+s
print("Самое маленькое число:", m)