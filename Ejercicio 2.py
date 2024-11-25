def solicitar_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Hay un error")


#################################################


a = solicitar_numero("Escribe un número: ")
b = solicitar_numero("Escribe otro número: ")

print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
try:
    print("a / b:", a / b)
except ZeroDivisionError:
    print("No se puede dividir por cero.")