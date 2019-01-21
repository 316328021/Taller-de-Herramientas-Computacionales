def mcd(a,b):
    if a<b: #Cambia el contenido de dos variables
        tmp = b
        b = a
        a = tmp
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a%b
    return b
