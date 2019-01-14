# -*- coding: utf-8 -*-
#Tarea 01. Problema de física
#García Rivas Brenda Paola
#La velocidad de una partícula que se mueve a lo largo del eje x varía de acuerdo con la espresión vx=(40-5t**2),donde vx está en m/s y t está en segundos.
#encontrar la aceleración promedio en el intervalo de tiempo t=0 a t=2.0s

"""Tarea01
print 40-5*0**2 #Cuando t=0
print 40-5*2.0**2 #Cuando t=2-0
print (20-40)/(2.0-0) #Aceleración promedio
q=40
w=5
t1=0
t2=2.0
#Para obtener cuando t=0
print q-w*t1**2
#Para obtener cuando t=2.0
print q-w*t2**2
#Para obtener aceleración 
vx1 = q-w*t1**2
vx2 = q-w*t2**2
print (vx2-vx1)/(t2-t1)"""

#Continuación de la tarea.
q=40
w=5
t1=0.0
t2=2.0
y1=q-w*t1**2
y2=q-w*t2**2
a=(y2-y1)/(t2-t1)
print 'La velocidad de la partícula en t1=%d es %d' % (t1,y1)#se usa %d porque da numeros enteros
def velocidad(t1,w):
    y=q-w*t1**2
    return(y)
print 'La velocidad de la partícula en t2=%d es %d' % (t2,y2)#se usa %d porque de un número entero
def velocidad(t2,w):
    y=q-w*t2**2
    return(y)
print 'La aceleración promedio de la parícula entre t1=%d y t2=%d es %d' % (t1,t2,a)#Se usa %d por ser enteros, además como son tres variables, entonces deben aparecer tres %d
def aceleracionPromedio (t1,t2,a):
    y=(y2-y1)/(t2-t1)
    return(y)


    




















