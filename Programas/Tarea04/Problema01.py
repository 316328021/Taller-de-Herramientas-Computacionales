# -*- coding: utf-8 -*-
"""
Tarea 4, Problema 01
Brenda Paola García Rivas
No cuenta: 316328021
Taller de Herramientas Computacionales
"""
#Hallar el máximo común múltiplo de una pareja de números enteros

MCD = False
N1= int(input('Primer número:'))
N2= int(input('segundo número:'))
if N1>0 and N2>0:
    if N1<N2:   #En caso de que N1 sea mayor a N2...
        c=N1
        N1=N2  #...Se hace un cambio de variable para tener el valor menor en N1
        N2=c
    i=N1

    while MCD == False and i>=1:
        if N1%i == 0 and N2%i == 0:
            print ('El MCD es',i)
            MCD = True

        else:
            i -=1
    
else:
    if N1 == N2:
        print ('Son los mísmos números')
    else:
        print('incorrecto')
    



