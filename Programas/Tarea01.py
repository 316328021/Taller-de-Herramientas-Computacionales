# -*- coding: utf-8 -*-
#Tarea 01. Problema de física
#García Rivas Brenda Paola
#La velocidad de una partícula que se mueve a lo largo del eje x varía de acuerdo con la espresión vx=(40-5t**2),donde vx está en m/s y t está en segundos.
#encontrar la aceleración promedio en el intervalo de tiempo t=0 a t=2.0s
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
print (vx2-vx1)/(t2-t1)
