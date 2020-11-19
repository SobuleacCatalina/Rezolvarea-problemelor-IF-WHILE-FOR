  
"""
Conform calendarului japonez, fiecare an poartă numele unui animal. Fiecare denumire se repetă exact o dată la 12 ani. Deci, un ciclu este 
format din 12 ani cu următoarele denumiri de animale în această ordine: șobolan,bou,tigru,iepure,dragon,șarpe,cal,oaie,maimuță,cocoș,câine,
porc. Știind că anul 2000 a fost anul Dragonului, să se scrie un algoritm care va citi de la tastatură anul (număr de patru cifre) și va afișa
denumirea lui conform calendarului japonez.
"""
a=eval(input("introdu anul: "))
if (a//1000==0):
    print("Introdu alt an")
elif (a%12==0):
    print("Anul Maimuței")
elif (a%12==1):
    print("Anul Cucoșului")
elif (a%12==2):
    print("Anul Câinelui")
elif (a%12==3):
    print("Anul Porcului")
elif (a%12==4):
    print("Anul Șobolanului")
elif (a%12==5):
    print("Anul Boului")
elif (a%12==6):
    print("Anul Tigrului")
elif (a%12==7):
    print("Anul Iepurelui")
elif (a%12==8):
    print("Anul Dragonului")
elif (a%12==9):
    print("Anul Șarpelui")
elif (a%12==10):
    print("Anul Calului")
else:
    print("Anul Oaiei")