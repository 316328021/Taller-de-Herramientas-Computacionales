# -*- coding: utf-8 -*-
Lista=[1,2,3,4,5,6,7,8,9,10]

"""
def printR(n):
    if n>0:
        printR(n-1)
        print n
printR (5)
printR (9)
printR (Lista)
"""

def printR(L):
    if L: #Si L tiene elementos
        print L[0],
        printR(L[1:])
    else:
        None 
printR([1,2,3,4,5,6,7,8,9,10])


def printR1(L):
    global T
    T=25
    if len(L)>1: #Si L tiene elementos
        print L[0],
        printR(L[1:])
    else:
        print(L[0])

def f1():
    return 2*x

printR([1,2,3,4,5,6,7,8,9,10])
printR1([1,2,3,4,5,6,7,8,9,10])

L=[-8,5,4,5,-3] #Si se coloca otra L, no importa porque no modifica a la L global
print '--------'
print L #Sólo aparece si se manda a imprimir, pero sigu7e sin afectar a la otra L
x=15
print f1()
print T

#http://www.pythontutor.com/visualize.html
