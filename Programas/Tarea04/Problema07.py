# -*- coding: utf-8 -*-
#Definir un función que identifique un número mayor de dos números

def mayor(a,b):
    if a > b:
        return a
    else:
        return b

#Para 3 números

def mayor2(a, b, c):
    if a > b and a>c:
        return a
    if b > a and b>c: #Aquí se puede usar elif
        return b
    else:
        return c
