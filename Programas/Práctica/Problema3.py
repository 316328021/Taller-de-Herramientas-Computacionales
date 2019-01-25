# -*- coding: utf-8 -*-
"""
Alumno: García Rivas Brenda Paola
No. cuenta: 316328021
Práctica/Examen
"""
#Problema3. Suma de los primeron n números al cubo.
#Tengo la idea de resolverlo con recursividad. Para eso se necesitan dos cosas:
#Ahora que he escrito en mi hoja de papel, creo que primero debo calcular el cubo de los números
#Para despues sumarlos
def SumaCubos(n):
    if n == 0:
        return 0   #1. Caso base
    else:
        return n**3 + SumaCubos(n-1)   #Regla Recursiva
    print SumaCubos(3)
    
        
