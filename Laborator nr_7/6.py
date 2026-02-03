# Задача 6. Să se elaboreze un program care afișează valorile funcției f(x)=3x^2+x+2 pe intervalul [-2; 5] cu pasul h=1, utilizând funcția definită.
def f(x):
    return 3*x*x+x+2

x=-2
while x<=5:
    y=f(x)
    print("f(", x,")=", y)
    x=x+1