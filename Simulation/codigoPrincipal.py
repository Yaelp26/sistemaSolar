import numpy as np
from planetComputing import codigoIntegracion as i
import codigoGraficacion as g

def initialize_state():   
    x1, y1 = 0.0, 0.0
    xp1, yp1 = 5e-06, 5e-06

    x2, y2 = 1, 0
    xp2, yp2 = 5e-06, 5e-06

    x3, y3 = 2, 0
    xp3, yp3 = 5e-06, 5e-06

    x4, y4 = 3, 0
    xp4, yp4 =  5e-06, 5e-06

    x5, y5 = 4, 0
    xp5, yp5 = 5e-06, 5e-06

    x6, y6 = 5, 0
    xp6, yp6 = 5e-06, 5e-06


    X = np.zeros(30)
    X[0], X[1] = x1, y1
    X[2], X[3] = x2, y2
    X[4], X[5] = x3, y3
    X[6], X[7] = x4, y4
    X[8], X[9] = x5, y5
    X[10], X[11] = x6, y6

    X[12], X[13] = xp1, yp1
    X[14], X[15] = xp2, yp2
    X[16], X[17] = xp3, yp3
    X[18], X[19] = xp4, yp4
    X[20], X[21] = xp5, yp5
    X[22], X[23] = xp6, yp6
  
    return X

# Condiciones iniciales
X = initialize_state()

# Parámetros de simulación
h = 10000e-3  # Paso de integración
N = 50e3      # Iteraciones

# Ajuste de masas de los planetas
m1, m2, m3, m4, m5 , m6= 1000, 1, 1, 1, 1 ,1  # Ajusta la masa del tercer planeta (m3)

# Integración y visualización
p1, p2, p3, p4, p5, p6 , N = i.runge_kutta_integration(X, h, int(N), m1, m2, m3, m4, m5,m6)
g.plot_animation(p1, p2, p3, p4, p5,p6, int(N))