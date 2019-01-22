# -*- coding: utf-8 -*-
"""García Rivas Brenda Paola
No. cuenta: 316328021
Clase 12
"""
alumnos = []
alumnos.append([9,8,10,9])
alumnos.append([9])
alumnos.append([6,9,10,8,9,10,10,9])
print alumnos

for i in range(len(alumnos)):#Se va a recorrer cada uno de los elementos de la lista
    for j in range(len(alumnos[i])):
        calificacion = alumnos[i][j] #de la iésima lista se obtiene el jésimo elemento. Esto es porque hay listas dentro la lsita
        print '%4d'% calificacion,
    print

#Hacer lista sin usar índice, es decir, sin usar range
for alumno in alumnos:
    for calificacion in alumno:
        print '%4d' % calificacion,
    print

        
"""for j in i:
    calificacion = alumnos[i][j]
    print '%4d'% calificacion,
print
""""       

