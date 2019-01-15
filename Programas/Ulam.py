# -*- coding: utf-8 -*-
def ulam(x):
    #if (x/2)*2-x==0:
    if x%2 == 0: #Al usar el %2 Estamos diciendo que el residuo de la división entre 2 es 0, es decir, que el numero es par
        return (x/2)#Si es par, retorna esto
    else: #Al no cumplir que sea 0 el residuo significa que es impar
        return (3*x+1)#Si es impar, retorna (3*x+1)

def suc(x):
    i=0# Cuenta número de veces que se ejecuta el ciclo
    #while x>1:
    while x!=1: #El número debe ser distino de 1, pues es el número al que se quiere llegar es este.
        x=ulam(x)#Se llama a la función
        i=i+1#Se le suma el nuero cada vez que termina el cilo
    return i
    
print ulam(52)
print suc(7)
print suc(26)
print suc(52)
print suc(1024)
print suc(72)
print suc(1524927)
print suc(2)

