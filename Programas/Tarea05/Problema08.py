# -*- coding: utf-8 -*-
"""
Alumna: García Rivas Brenda Paola
No.cuenta:316328021
Tarea 05
Problema 08
"""
#Definir una función que devuelva 'false' si es un carácter y 'True' si es una vocal
def vocal(caracter):
    lista_v=['a','e','i','o','u']
    for vocales in lista_v:
        if caracter == vocales:
            return True
    else:
        return False
