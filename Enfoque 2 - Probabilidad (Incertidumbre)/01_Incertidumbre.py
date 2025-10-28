# Enfoque 2 - Incertidumbre
#3Farid Ariel Orozco Sanchez - 21310200
# 6 E2 2do Parcial

import numpy as np                       # importa NumPy, biblioteca para cálculo numérico y arreglos
import matplotlib.pyplot as plt          # importa matplotlib.pyplot para crear gráficos
from scipy.stats import binom            # importa la distribución binomial de scipy.stats

n_lanzamientos = 10                      # número total de lanzamientos de la moneda
probabilidad_exito = 0.5                 # probabilidad de éxito en cada ensayo (cara = 0.5)

x = np.arange(0, n_lanzamientos + 1)     # vector con todos los posibles éxitos: 0,1,...,10

probabilidades = binom.pmf(x, n_lanzamientos, probabilidad_exito)
# calcula la PMF (probabilidad de masa) de la binomial para cada k en x
# devuelve un arreglo con P(X = k) para k = 0..10

plt.figure(figsize=(10, 6))              # crea una nueva figura de tamaño 10x6 pulgadas

plt.stem(x, probabilidades,               # dibuja un gráfico de tallo: marcas discretas con líneas
         basefmt=" ",                     # basefmt=" " elimina la línea base horizontal
         use_line_collection=True)        # mejora la eficiencia del dibujo para muchos puntos

plt.xlabel("Número de éxitos (caras)")    # etiqueta del eje x
plt.ylabel("Probabilidad")                # etiqueta del eje y
plt.title("Distribución Binomial: Probabilidad de obtener caras en lanzamientos de moneda")
# título de la gráfica

plt.grid(True)                            # activa la cuadrícula para facilitar la lectura
plt.show()                                # muestra la figura en pantalla
