import random
import string

def generar_contrasena():
    longitud = int(input("Longitud de la contraseña: "))
    mayusculas = int(input("Cantidad de letras mayúsculas: "))
    minusculas = int(input("Cantidad de letras minúsculas: "))
    numeros = int(input("Cantidad de números: "))
    especiales = int(input("Cantidad de caracteres especiales: "))

    # Comprueba que la longitud de la contraseña
    if longitud < mayusculas + minusculas + numeros + especiales:
        print("La longitud de la contraseña debe ser mayor o igual a la suma de las cantidades especificadas.")
        return None

    caracteres_mayusculas = string.ascii_uppercase
    caracteres_minusculas = string.ascii_lowercase
    caracteres_numeros = string.digits
    caracteres_especiales = string.punctuation

    if mayusculas > len(caracteres_mayusculas):
        print("La cantidad de letras mayúsculas especificada es mayor de la disponible.")
        return None
    if minusculas > len(caracteres_minusculas):
        print("La cantidad de letras minúsculas especificada es mayor de la disponible.")
        return None
    if numeros > len(caracteres_numeros):
        print("La cantidad de números especificada es mayor de la disponible.")
        return None
    if especiales > len(caracteres_especiales):
        print("La cantidad de caracteres especiales especificada es mayor de la disponible.")
        return None

    # Genera aleatoriamente los caracteres
    contrasena = ''.join(random.choice(caracteres_mayusculas) for _ in range(mayusculas))
    contrasena += ''.join(random.choice(caracteres_minusculas) for _ in range(minusculas))
    contrasena += ''.join(random.choice(caracteres_numeros) for _ in range(numeros))
    contrasena += ''.join(random.choice(caracteres_especiales) for _ in range(especiales))


    while len(contrasena) < longitud:
        tipo_caracter = random.choice([caracteres_mayusculas, caracteres_minusculas, caracteres_numeros, caracteres_especiales])
        contrasena += random.choice(tipo_caracter)

    contrasena = ''.join(random.sample(contrasena, len(contrasena)))

    return contrasena

contrasena_generada = generar_contrasena()
if contrasena_generada:
    print("Contraseña generada:", contrasena_generada)