st="Hafta=4, Gun=1, Saat=9, Dakika=3"
#Bu format� t�m de�erleri 1 artt�rarak Hafta=5-Gun=2-Saat=10-Dakika=4

print "Orijinal=>",st

stl=st.split(",") #�nce virg�le gore ay�r�yoruz.
print "Virg�le g�re parse edilmi� hali=>",st
yeni=""

for i in st1:
    temp=i.split("=")
    yeni+=(temp[0]+":"+str(int(temp[1])+1))
    #yeni+=":".join([temp[0],str(int(temp[1]+1))]

yeni="-".join(yeni.split(" ") #�nce bo�lu�a g�re split et, - ile
print "De�i�tirilmi� hali=>", yeni
