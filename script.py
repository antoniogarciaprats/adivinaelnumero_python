
#Pequeño programa que simula un juego en el que adivinas un número
#y tienes varios intentos para adivinarlo

#Antonio García Prats

import random

secretnumber = random.randint(1, 10)
attemps = 3

print ("Piensa un número entre 1 y 10. Tienes 3 intentos para adivinarlo.")

while attemps > 0:
    guess = int(input("Realiza un intento para adivinarlo: "))
    if guess == secretnumber:
        print ("Felicitaciones, has adivinado el número")
        break
    elif guess < secretnumber: print("El número que has introducido es menor")
    else: print("El número es mayor que el que tienes que adivinar")
    attemps -= 1

if attemps == 0: print ("Lo siento, Has agotado todos los intentos. El númeor secreto era igual a: ",secretnumber)





