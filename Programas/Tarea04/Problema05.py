# -*- coding: utf-8 -*-
"""
Tarea 4, Problema 05
Brenda Paola García Rivas
No cuenta: 316328021
Taller de Herramientas Computacionales
"""
#Culcular la suma de los primeros n enteros
def sumar(n):
    return (n * (n+1)) / 2 #Fórmula
n = int(input('Ingrese un número natural: '))
suma= sumar(n)
print ('Resultado: ', suma)


