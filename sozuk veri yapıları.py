sozluk={"isim":"Python",
        "dogumyili":"1990",
        "nesne":True,
        "versiyon":3}


#s�zl�k �zerinde d�ng�
print "tipi=",type(sozluk)

for (k,v) in sozluk.items():
    print k,"=>",v

print sozluk["versiyon"]         #spesifik bit anahtar�n de�erine eri�mek
sozluk["gelistirici"]="Rossum"   #yeni key:value ilave etmek
sozluk["dogumyili"]="1991"

print sozluk                     #s�zl��� tek seferde yazd�rmak
print len(sozluk)

print sozluk.keys()
print sozluk.values()
