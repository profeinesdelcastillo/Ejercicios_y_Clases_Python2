def superior(funcion,lista):
    nueva = []
    for n in lista:
        nueva.append(funcion(n))
    return nueva


######################################


print(superior(lambda x : x**3,[1,2,3]))

