import numpy as np
from planetComputing import codigoIntegracion as i
import codigoGraficacion as g

def initialize_state():   
    x1, y1 = 0.1, 0.1
    xp1, yp1 = 5e-06, -5e-06

    x2, y2 = 0, 0
    xp2, yp2 = 5e-06, 0

    x3, y3 = -0.1, -0.1
    xp3, yp3 = -5e-06, 5e-06

    X = np.zeros(12)
    X[0], X[1], X[2], X[3], X[4], X[5] = x1, y1, x2, y2, x3, y3
    X[6], X[7], X[8], X[9], X[10], X[11] = xp1, yp1, xp2, yp2, xp3, yp3

    return X

# Condiciones iniciales
X = initialize_state()

# Parámetros de simulación
h = 1000e-3  # Paso de integración
N = 50e3     # Iteraciones
m1, m2, m3 = 1, 1, 1

# Integración y visualización
p1, p2, p3, N = i.runge_kutta_integration(X, h, int(N), m1, m2, m3)
g.plot_animation(p1, p2, p3, int(N))