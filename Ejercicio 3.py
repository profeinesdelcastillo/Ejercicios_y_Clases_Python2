paises = {
    "ar": "Argentina",
    "es": "España",
    "us": "Estados Unidos",
    "fr": "Francia"
}

while True:
    codigo = input("Ingrese un codigo: ")
    if codigo == "salir":
        break
    try:
        print(paises[codigo])
    except KeyError:
        print("El código es invalido, vuelve a intentarlo.")