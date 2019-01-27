# -*- coding: utf-8 -*-
"""
Brenda Paola García Rivas
No. cuenta: 316328021
Tarea05
Problema9
"""
#Invertir una lista
def invertida(lista):
    lista1=[]   #Creamos una lista vacía
    for n in lista: #Para cada valor n en la lista 
        lista1.insert(0,n) #Lo insertará en la lista1
    return lista1 #DEvuelve la lista 
