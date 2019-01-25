# -*- coding: utf-8 -*-
"""
Exámen Práctico
Taller de Herramientas Computacionales
García Rivas Brenda Paola
No. cuenta: 316328021
"""
#Problema6. Calcular factorial de un número n
#Debemos tener en cuenta que se necesitan dos cosas:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
        print factorial(2)

