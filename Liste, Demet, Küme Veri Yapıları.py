liste=[3,1,"b",5,"a",10,2,3,5]
demet=(3,1,5,"a",10,2,3,5)
kume={3,1,5,10,2,3,5}

print ("Tipler", type(liste), type(demet), type(kume))

liste.pop()
liste.append(20)
liste.sort()

print ("liste")
for i in liste:
    print (i)
    
print ("demet")
for i in demet:
    print (i)
    
kume.pop()
kume.add("b")

print ("kume")
for i in kume:
    print (i)
