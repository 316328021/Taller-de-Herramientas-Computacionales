# -*- coding: utf-8 -*-
def vAbsoluto(x):
	if x>=0:
		return(x)
	else:
		return(-x)
def raiz(x):
        h=x
        b=1.0
        e=0.0001
        while vAbsoluto(b-h)>e:
                h = (b+h)/2
                b = x/h
                return (b) #Se puede cualquiera de los dos, b o h, ya que son similares

def raiz1(x):
        h=x
        b=1.0
        e=0.0001
        i=0 #Cuenta el número de veces que se ejecuta el ciclo
        while vAbsoluto(b-h)>e:
                h = (b+h)/2
                b = x/h
                i=i+1
        print"El ciclo se repitió %d veces"% (i)
        return (b)

print raiz1(1)
print raiz1(4)
print raiz1(9)
print raiz1(9.1)
print raiz1(1000000)

