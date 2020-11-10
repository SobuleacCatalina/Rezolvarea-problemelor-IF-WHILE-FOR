"""
Se dau numerele reale pozitive a,b,c. Să se verifice dacă un triunghi ale cărui laturi au lungimile (în aceeași unitate de măsură) egale 
cu a,b,c. În caz afirmativ, să se determine tipul triunghiului: echilteral,isoscel,scalen.
"""
a=int(input("Introdu numărul a: "))
b=int(input("Introdu numărul b: "))
c=int(input("Introdu numărul c: "))
if ((a+b>c)and(a+c>b)and(b+c>a)):
    if ((a==b)and(a==c)and(b==c)):
        print("Formeaza un triunghi echilateral")
    elif ((a!=b)and(a!=c)and(b!=c)):
        print("Formeaza un triunghi scalen")
    else:
        print("Formeaza un triunghi isoscel")
else:
    print("Nu formeaza un triunghi")