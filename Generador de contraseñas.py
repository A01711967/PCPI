import random
import string

def generar_contrasena():
    longitud = int(input("Longitud de la contraseña deseada: "))
    mayusculas = int(input("Cantidad de letras mayúsculas deseadas: "))
    minusculas = int(input("Cantidad de letras minúsculas deseadas: "))
    numeros = int(input("Cantidad de números deseados: "))
    especiales = int(input("Cantidad de caracteres especiales deseados: "))

    caracteres = ''
    
    if mayusculas > 0:
        caracteres += ''.join(random.choice(string.ascii_uppercase) for _ in range(mayusculas))
    if minusculas > 0:
        caracteres += ''.join(random.choice(string.ascii_lowercase) for _ in range(minusculas))
    if numeros > 0:
        caracteres += ''.join(random.choice(string.digits) for _ in range(numeros))
    if especiales > 0:
        caracteres += ''.join(random.choice(string.punctuation) for _ in range(especiales))

    while len(caracteres) < longitud:
        caracteres += random.choice(string.ascii_letters + string.digits + string.punctuation)
    
    contrasena = ''.join(random.sample(caracteres, len(caracteres)))
    
    return contrasena

contrasena_generada = generar_contrasena()
print("Contraseña generada:", contrasena_generada)
