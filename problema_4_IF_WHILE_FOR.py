"""
Să se scrie un program care va efectua:
a) adunarea a două fracții date;
b) înmulțirea a două fracții date;
Rezultatul va fi o fracție ireductibilă.
"""
m1=eval(input("Introdu prima fractie: "))
n1=eval(input(""))
m2=eval(input("Introdu a doua fractie: "))
n2=eval(input(""))
ms=0
ns=0
if n1==n2:
    ms=m1+m2
    ns=n1
else:
    ms=m1*n2+m2*n1
    ns=n1*n2
mp=m1*m2
np=n1*n2
m=ms
n=ns
while n!=0:
    c=m%n
    m=n
    n=c
if ns//m==1:
    print("a)",m1,"/",n1,"+",m2,"/",n2,"=",ms//m)
else:
    print("a)",m1,"/",n1,"+",m2,"/",n2,"=",ms//m,"/",ns//m)
m=mp
n=np
while n!=0:
    c=m%n
    m=n
    n=c
if np//m==1:
    print("b)",m1,"/",n1,"x",m2,"/",n2,"=",mp//m)
else:
    print("b)",m1,"/",n1,"x",m2,"/",n2,"=",mp//m,"/",np//m)