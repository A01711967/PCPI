import random
import string

def generar_contrasena():
    longitud = int(input("Longitud de la contraseña: "))
    mayusculas = int(input("Cantidad de letras mayúsculas: "))
    minusculas = int(input("Cantidad de letras minúsculas: "))
    numeros = int(input("Cantidad de números: "))
    especiales = int(input("Cantidad de caracteres especiales: "))

    if longitud < mayusculas + minusculas + numeros + especiales:
        print("La longitud de la contraseña debe ser mayor o igual a la suma de las cantidades especificadas.")
        return None

    carac_may = string.ascii_uppercase
    carac_min = string.ascii_lowercase
    carac_num = string.digits
    carac_esp = string.punctuation

    if mayusculas > len(carac_may):
        print("La cantidad de letras mayúsculas especificada es mayor de la disponible.")
        return None
    if minusculas > len(carac_min):
        print("La cantidad de letras minúsculas especificada es mayor de la disponible.")
        return None
    if numeros > len(carac_num):
        print("La cantidad de números especificada es mayor de la disponible.")
        return None
    if especiales > len(carac_esp):
        print("La cantidad de caracteres especiales especificada es mayor de la disponible.")
        return None

    contrasenas = []

    for _ in range(4):
        contrasena = ''.join(random.choice(carac_may) for _ in range(mayusculas))
        contrasena += ''.join(random.choice(carac_min) for _ in range(minusculas))
        contrasena += ''.join(random.choice(carac_num) for _ in range(numeros))
        contrasena += ''.join(random.choice(carac_esp) for _ in range(especiales))

        while len(contrasena) < longitud:
            tipo_caracter = random.choice([carac_may, carac_min, carac_num, carac_esp])
            contrasena += random.choice(tipo_caracter)

        contrasena = ''.join(random.sample(contrasena, len(contrasena)))
        contrasenas.append(contrasena)

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