# -*- coding: utf-8 -*-
"""
Tarea 4, Problema 03
Brenda Paola García Rivas
No. cuenta: 316328021
Taller de Herramientas computacionales
"""
#Dado un número natural, calcular el décimo elemento de la sucesión de Fibonacci
#Se sabe que la serie de fibonacci son los dos numeros anteriores sumados, se empieza con 1+1=2, el siguiente sería 1+2=3, etc.
#Tomamos los dos primeros números
Num1=1
Num2=1
print Num1
print Num2
i=0 #Se inica con este número
n=10 #Se pide el décimo número de la serie
while i<n: #Se dice que mientras i sea menor que n, pero mayor a 1se cumplirá que:
    F=Num1+Num2  #Fibonacci es igual a el numero más el número 2
    Num1=Num2 #Como la suma se va recorriendo, queda que:
    Num2=F
    print F
    i+=1 #Se le va sumando a i

#Para preguntar por el número

Fibonacci= int(input('Número entero'))
if Fiboncci < 0:
    print ('Ingrese otro número')
    
    
