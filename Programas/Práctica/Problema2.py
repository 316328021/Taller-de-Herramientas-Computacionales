# -*- coding: utf-8 -*-
"""
Exámen Práctico
Taller de Herramientas Computacionales
García Rivas Brenda Paola
No. cuenta: 316328021
"""
#Problema2. Calcular la suma de los primeros n enteros
""" Primer intento.
def suma_enteros(n):
    s=0
    for i in range (n+1):
        s +=1
    print s
"""
"""Segundo intento.
def suma_enteros(n):
    i=0
    while suma !=0:
        i +=1

    print ('R= ')
"""
#Para que sea de forma recursiva, necesita contar con dos cosas:

def suma(n):
    if n == 0:  #Caso base
        return 0
    else:
        return n + suma(n-1)  #Regla de recursividad
        print suma(n)
#print ('Numero natural: ',n,)  No puedo hacer que pregunte :(, pero sí funciona :)
