import random
liste=list()
for i in range(random.randint(1,1000)):
    liste.append(random.random())
x,s=len(liste),sum(liste)
print x, "tane elemandan olu�an listenin toplam�=", s, "ortalamas�=", s/x
