#k�sa yol

x=[1./i**2 for i in range (1,100) if i%2==0]
print x

#uzun yol

x=list()
for i in range(1,100):
    if i%2==0:
        x.append(1./i**2)

print x
