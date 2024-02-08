import numpy as np
from planetComputing import codigoIntegracion as i
import codigoGraficacion as g

def initialize_state():
    x1, y1 = 0.1, 0.1
    xp1, yp1 = 5e-06, -5e-06

    x2, y2 = 0, 0
    xp2, yp2 = 5e-06, 0

    X = np.zeros(8)
    X[0], X[1], X[2], X[3] = x1, y1, x2, y2
    X[4], X[5], X[6], X[7] = xp1, yp1, xp2, yp2

    return X

# Condiciones iniciales
X = initialize_state()

# Parámetros de simulación
h = 1000e-3  # Paso de integración
N = 50e3     # Iteraciones
m1, m2 = 1, 1

# Integración y visualización
p1, p2, N = i.runge_kutta_integration(X, h, int(N), m1, m2)
g.plot_animation(p1, p2, int(N))
