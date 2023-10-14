import random
import string

def generar_contrasena():
    longitud = int(input("Longitud de la contraseña: "))
    requisitos = {
        "mayusculas": int(input("Cantidad de letras mayúsculas: ")),
        "minusculas": int(input("Cantidad de letras minúsculas: ")),
        "numeros": int(input("Cantidad de números: ")),
        "especiales": int(input("Cantidad de caracteres especiales: "))
    }

    if longitud < sum(requisitos.values()):
        print("La longitud de la contraseña debe ser mayor o igual a la suma de las cantidades especificadas.")
        return None

    caracteres = {
        "mayusculas": list(string.ascii_uppercase),
        "minusculas": list(string.ascii_lowercase),
        "numeros": list(string.digits),
        "especiales": list(string.punctuation)
    }

    for clave, valor in requisitos.items():
        if valor > len(caracteres[clave]):
            print(f"La cantidad de {clave} especificada es mayor de la disponible.")
            return None

    contrasenas = []

    for _ in range(4):
        contrasena = []

        for clave, valor in requisitos.items():
            contrasena.extend(random.sample(caracteres[clave], valor))

        while len(contrasena) < longitud:
            tipo_caracter = random.choice(list(caracteres.values()))
            contrasena.append(random.choice(tipo_caracter))

        random.shuffle(contrasena)
        contrasenas.append(''.join(contrasena))

    print("Contraseñas generadas:")
    for i, contrasena in enumerate(contrasenas):
        print(f"{i + 1}: {contrasena}")

    seleccion = int(input("Selecciona la contraseña que deseas usar (1, 2, 3 o 4): "))
    if 1 <= seleccion <= 4:
        return contrasenas[seleccion - 1]
    else:
        print("Selección inválida. Se utilizará la primera contraseña.")
        return contrasenas[0]

contrasena_generada = generar_contrasena()
if contrasena_generada:
    print("Contraseña seleccionada:", contrasena_generada)
