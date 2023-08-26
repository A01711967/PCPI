import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@#$%^&*()<>,.:;[]"

string = lower + upper + symbols + numbers
length = 12
password = "".join(random.sample(string,length))

print("Tu contraseña es:" + password)
