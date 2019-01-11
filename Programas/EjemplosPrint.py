# -*- coding: utf-8 -*-
i = 62
r = 189876545.7654675432

# Print out numbers with quotes "" such that we see the
# width of the field
print '"%d"' % i       # minimum field
#Se visualiza el mínimo numero de enteros
print '"%5d"' % i      # field of width 5 characters
#Se imprimen enteros con 5 caracteres
print '"%05d"' % i     # pad with zeros
#Se imprimen enteros con ceros
print '"%g"' % r       # r is big number so this is scientific notation
#Se imprime el número flotante
print '"%G"' % r       # E in the exponent
#Se visualiza el exponente 
print '"%e"' % r       # compact scientific notation
#Se visualiza el número flotante como notación científica
print '"%E"' % r       # compact scientific notation
#Se imprime el número flotante como notación científica
print '"%20.2E"' % r   # 2 decimals, field of width 20
#Se visualizan 2 decimales y 20 enteros 
print '"%30g"' % r     # field of width 30 (right-adjusted)
#Se imprimen 30 números flotantes hacia la derecha  
print '"%-30g"' % r    # left-adjust number
#Se visualizan 30 mnúmeros flotantes hacia la izquierda 
print '"%-30.4g"' % r  # 3 decimals

print '%s' % i   # can convert i to string automatically
#Visualiza una cadena de un entero
print '%s' % r
#visualiza la cadena de un flotante

# Use %% to print the percentage sign
print '%g %% of %.2f Euro is %.2f Euro' % \
      (5.1, 346, 5.1/100*346)
