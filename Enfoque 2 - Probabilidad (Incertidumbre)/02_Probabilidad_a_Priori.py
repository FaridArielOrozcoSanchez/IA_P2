# Enfoque 2 - Probabilidad (Incertidumbre)
#3Farid Ariel Orozco Sanchez - 21310200
# 6 E2 2do Parcial

import numpy as np                              # importa NumPy para operaciones numéricas y generación de datos aleatorios
import matplotlib.pyplot as plt                 # importa matplotlib.pyplot para crear gráficos
from collections import Counter                 # importa Counter para contar ocurrencias de elementos en una lista/array

np.random.seed(42)                               # fija la semilla del generador aleatorio para reproducibilidad (misma salida cada vez)
datos = np.random.choice(['A', 'B'],             # genera una muestra aleatoria de etiquetas 'A' y 'B'
                         size=100,               # tamaño de la muestra: 100 elementos
                         p=[0.7, 0.3])          # probabilidades de selección: P('A')=0.7, P('B')=0.3

conteo = Counter(datos)                          # cuenta cuántas veces aparece cada etiqueta en 'datos' (ej. {'A': 70, 'B': 30})
total = len(datos)                               # calcula el total de observaciones (aquí 100)

probabilidades_a_priori = {                       # construye un diccionario con las probabilidades a priori por clase
    clase: conteo[clase] / total                 # para cada clase, prob = conteo_clase / total
    for clase in conteo                           # itera sobre las claves (clases) encontradas en 'conteo'
}

print("Probabilidades a Priori:")                 # imprime un encabezado informativo
for clase, probabilidad in probabilidades_a_priori.items():  # recorre las clases y sus probabilidades
    print(f"Clase {clase}: {probabilidad:.2f}")   # imprime la probabilidad formateada con 2 decimales

plt.bar(probabilidades_a_priori.keys(),          # crea un gráfico de barras usando las clases como etiquetas x
        probabilidades_a_priori.values(),        # alturas de las barras = probabilidades a priori
        color=['blue', 'orange'])                # colores de las barras (opcional)
plt.xlabel('Clase')                              # etiqueta del eje x
plt.ylabel('Probabilidad a Priori')              # etiqueta del eje y
plt.title('Probabilidades a Priori de Clases Simuladas')  # título del gráfico
plt.show()                                       # muestra el gráfico en pantalla
