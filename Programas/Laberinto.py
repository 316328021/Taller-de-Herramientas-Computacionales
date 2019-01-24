# -*- coding: utf-8 -*-
L=[[True, True, True, True],
   [False, False, False, True],
   [True, True, False, True]]
"""def resolver(L,e):
    type(L)
    type(e)
    n=len(L[0])  #Columna 1
    x=e[0]
    y=e[1]
    if y==n-1:
        return e[0]+1,e[1]+1  #Ya llegué
    else: #Si no se ha llegado...
        if L[x][y+1] == False: #Se puede mover una columna más, por eso se aumenta a y 
            e=[x,y+1]
            return resolver(L,e)
        else:
            print 'Ya no se puede avanzar'"""

def abajo (L,e):
    type (L)
    type (e)
    n=len(L[0])
    x=e[0]
    y=e[1]
    if y==n-1:
        return e[0]+1, e[1]+1
    else:
        if L[x+1][y] == False:
            e=[x+1, y]
            return abajo(L,e)
        else:
            print "Ya no se puede avanzar" 

type(L)
e=[1,0]
r=abajo(L,e)
