#!/usr/bin/env python

# x1 rigth curves
# y1 left curves

# por cada curva derecha x1 gana x2 metros
# por cada curva izquierda y1 gana y2 metros
# la velocidad es S km

# La carrera tiene Z km
# Cada Z1 km ambos conductores paran y tardan x3 e y3 segundos (slo pasa si la distancia faltante es mayor al pit, NO si son iguales).
# s velocidad de cada uno en lnea recta

import math

x1 = int(input())
y1 = int(input())
x2 = int(input())           		# meters
y2 = int(input())           		# meters
z = int(input()) * 1000     		# meters
z1 = int(input()) * 1000    		# meters
x3 = int(input())           		# sec
y3 = int(input())           		# sec
s = int(input()) * 1000 / 3600  	# meters / sec

# Metros que gana cada jugador por las curvas
mx = x1 * x2
my = y1 * y2

# Tiempo perdido por pitstops
# Cuantas paradas
pit = z/z1
if (float(pit) == float(z/z1)):
	pit -= 1
pit = int(pit)

mx -= pit * x3 * s
my -= pit * y3 * s

if mx > my:
	print("Right Hand driver wins race by " + str(math.ceil(abs(mx-my))) + " meters")
elif my > mx:
	print("Left Hand driver wins race by " + str(math.ceil(abs(mx-my))) + " meters")
else:
	print("Race Drawn")