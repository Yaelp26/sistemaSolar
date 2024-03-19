import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import solve_ivp

# Constantes
G = 6.67430e-11  # Constante gravitatoria
masa_sol = 1.989e30  # Masa del Sol en kg
escala = 1.496e11  # Escala para ajustar las unidades de distancia

# Datos de los planetas (distancia inicial, velocidad inicial)
# Distancias en metros, velocidades en m/s
datos_planetas = {
    'Mercurio': [0.39, 47.87],
    'Venus': [0.72, 35.02],
    'Tierra': [1.0, 30.0],
    'Marte': [1.52, 24.08],
    'Jupiter': [5.20, 13.07],
    'Saturno': [9.58, 9.69],
    'Urano': [19.18, 6.81],
    'Neptuno': [30.07, 5.43]
}


def movimiento_planetas(t, y):
    dydt = np.zeros_like(y)

    num_planetas = len(datos_planetas)

    for i in range(num_planetas):
        xi, yi, vxi, vyi = y[i * 4:(i + 1) * 4]
        ax = 0
        ay = 0

        # Solo calculamos la interacción con el Sol, que asumimos está en el origen
        rij_x = xi
        rij_y = yi
        rij = np.sqrt(rij_x**2 + rij_y**2)

        # La aceleración debe ser negativa porque la fuerza gravitatoria es una fuerza de atracción.
        ax -= (G * masa_sol * rij_x) / rij**3
        ay -= (G * masa_sol * rij_y) / rij**3

        dydt[i * 4] = vxi
        dydt[i * 4 + 1] = vyi
        dydt[i * 4 + 2] = ax
        dydt[i * 4 + 3] = ay

    return dydt


# Condiciones iniciales
condiciones_iniciales = []

for planeta, datos in datos_planetas.items():
    x0 = datos[0] * escala  # Ajuste de escala
    v0 = datos[1] * 1000  # Convertir a m/s
    condiciones_iniciales.extend([x0, 0, 0, v0])

# Tiempo de simulación
t_inicio = 0
t_fin = 165 * 525600  # Simulación de 165 años en minutos
# Aumentamos el número de puntos de evaluación en el tiempo
t_eval = np.linspace(t_inicio, t_fin, 1000)  # Reducir el número de puntos

# Realizar la simulación
solucion = solve_ivp(movimiento_planetas, [
    t_inicio, t_fin], condiciones_iniciales, t_eval=t_eval, method='DOP853', rtol=1e-10, atol=1e-10)

# Preparar la figura para la animación
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlabel('Distancia (UA)')  # Etiqueta del eje x
ax.set_ylabel('Distancia (UA)')  # Etiqueta del eje y
ax.set_title('Simulación del Sistema Solar')  # Título del gráfico

# Representación del Sol en el gráfico
ax.scatter(0, 0, color='yellow', s=100, marker='o', label='Sol')

# Ajustar los límites de los ejes x e y
ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)

# Preparar los puntos para cada planeta
points = []
for planeta in datos_planetas.keys():
    point, = ax.plot([], [], 'o', markersize=3, label=planeta)
    points.append(point)

# Función de inicialización para la animación
def init():
    for point in points:
        point.set_data([], [])
    return points

# Función de animación
def animate(i):
    for j, point in enumerate(points):
        indice_inicio = j * 4
        x = solucion.y[indice_inicio][i] / escala  # Ajuste de escala
        y = solucion.y[indice_inicio + 1][i] / escala  # Ajuste de escala
        point.set_data(x, y)
    return points

# Crear la animación
ani = animation.FuncAnimation(fig, animate, frames=len(t_eval), init_func=init, blit=True)

# Mostrar la leyenda
ax.legend()

plt.show()
