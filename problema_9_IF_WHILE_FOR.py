"""
Un număr natural se numește număr perfect dacă este egal cu suma divizorilor lui, în afară de el însuși. De exemplu, 6 este număr perfect ,
deoarece 6=1+2+3. Să se afle numerele perfecte mai mici decât numărul natural dat n.
"""
n=int(input("Introdu numărul: "))
for p in range(1,n):
    s=0
    for i in range(1,p):
        if (p%i==0):
            s+=i
    if s==p:
        print(p,end=" ")
