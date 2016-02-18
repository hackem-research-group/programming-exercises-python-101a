#!/usr/bin/python
import random
inicio=0
fin=100
numrandomico=random.randint(inicio, fin)
x=inicio
y=x+20
def vrandom(x,y):
    flag=1
    while y <= fin and flag==1:
        if numrandomico>=x and numrandomico<=y:
            print "El numero ",numrandomico," esta en el rango de ",x," al ",y
            flag=0
        else:
            x=y
            y=x+20

vrandom(x,y)
