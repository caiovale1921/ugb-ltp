# Calcule o volume do cilindro de raio 6 cm e altura 5 cm (V = pi*r2*h).

import math

raio = float(input("Insira o valor do raio: "))
altura = float(input("Insira o valor da altura: "))

print ("Volume do cilindro:", math.pi*(raio**2)*altura)