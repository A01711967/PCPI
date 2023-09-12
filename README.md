Este proyecto ayuda con la generacion de contraseñas seguras para aquellos usuarios que desean una sin el uso de datos personales o que simplemente necesitan una sin necesidad de hacerla ellos mismos. Se pediran si el usuario lo desea requisitos para la contraseña y el programa entrega una que cumpla con los requisitos.


Proseso:
Definir Requisitos: Comienza ingresando los requisitos para las contraseñas que deseas generar. Estos requisitos pueden incluir la longitud deseada de la contraseña y los tipos de caracteres permitidos, como letras mayúsculas, minúsculas, números y símbolos.
Seleccionar Caracteres: Basado en los requisitos previos, crear un conjunto de caracteres permitidos que se utilizarán para construir las contraseñas. Esto podría incluir letras mayúsculas, letras minúsculas, dígitos
numéricos y símbolos especiales.
Dar Aleatoriedad: Una vez definido los caracteres para generar la contraseña se utiliza fuente para darle un aleatoridad a los caracteres utilizados en la contraeña.
Generar Contraseña: Utiliza los caracteres aleatorios seleccionados para construir la contraseña. Puede hacerlo eligiendo caracteres de manera secuencial o al azar.
Validación: Si tienes requisitos específicos para la contraseña, como la inclusión de al menos un número o un símbolo, valida la contraseña generada para asegurarte de que cumpla con esos requisitos. Si no cumple, se repite el procesoimport random



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
