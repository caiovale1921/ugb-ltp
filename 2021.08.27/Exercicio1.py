# Calcule e exiba a área do círculo (A = pi*r2) de qualquer raio que for digitado.

import math

while True:
    raio = float(input("Insira o valor do raio: "))
    print ("Área do circulo:", math.pi*(raio**2), "m")