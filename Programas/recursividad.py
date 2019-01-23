# -*- coding: utf-8 -*-
def fib(n):
    if n>2:
        """Calcula es nésimo término
de la sucesión de Fibonacci con n natural
"""
        return fib(n-1)+ fib(n-2)
    else:
        return 1

def suma(n):
    if  n>1:
        """Calcula el nésimo término
de la sucesión de la suma de los primeros n naturales
"""
        return n + suma(n-1)
    else:
        return 1

L=[1,2,3,4,5,6,7,8,9,10]
def printR (n):
    for n in L:
        print n
    

fib (1)
fib (2)
fib (5)
fib (10)


suma (1)
suma (5)
suma (10)
