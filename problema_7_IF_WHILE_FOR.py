"""
Mihai are un unchi bogat care i-a dăruit în ziua când s-a născut un dolar, iar în fiecare an următor el dubla cadoul și mai adăuga atâția 
dolari câți ani implinea Mihai.
a)Să se calculeze câți dolari a pimit Mihai atunci când împlinit n ani (n<20).
b)La ce vârstă cadoul lui Mihai a fost mai mare de 100$?
"""
n=int(input("Introdu numărul: "))
s=1
s2=1
h=0
for i in range(1,n+1):
    s=s*2+i
print("a)Cand Mihai a împlinit",n,"ani, a primit",s,"dolari")
while s2<=100:
    h+=1
    s2=s2*2+h
print("b)Cadoul lui Mihai a fost mai mare de 100$,când a împlinit",h,"ani")