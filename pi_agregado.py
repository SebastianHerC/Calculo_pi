import random
import numpy as np
import matplotlib.pyplot as plt

contador_d = 0
contador_t = 0
dentro_circulo_x = []
dentro_circulo_y = []
fuera_circulo_x = []
fuera_circulo_y = []

for i in range(0, 10000):
    coordenada_x = random.uniform(-1, 1)
    coordenada_y = random.uniform(-1, 1)
    cond = coordenada_x**2 + coordenada_y**2
    contador_t += 1
    if cond < 1:
        contador_d += 1
        dentro_circulo_x.append(coordenada_x)
        dentro_circulo_y.append(coordenada_y)
    else:
        fuera_circulo_x.append(coordenada_x)
        fuera_circulo_y.append(coordenada_y)

pi = (contador_d*4) / contador_t
diferencia = abs(np.pi - pi)
porcentaje = (diferencia * 100) / np.pi

print("Valor aproximado de pi:", pi)
print(f"diferencia entre numpy.py y pi calculado = {diferencia}")
print("{:.2f}%".format(porcentaje))

# Gráfico
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_aspect('equal', adjustable='box')
ax.scatter(dentro_circulo_x, dentro_circulo_y, color='blue', label='Dentro del círculo')
ax.scatter(fuera_circulo_x, fuera_circulo_y, color='red', label='Fuera del círculo')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('Coordenada X')
ax.set_ylabel('Coordenada Y')
ax.set_title('Aproximación de Pi mediante Monte Carlo')
ax.add_artist(plt.Circle((0, 0), 1, color='black', alpha=0.1, label='Círculo unitario'))
ax.legend()

plt.show()
