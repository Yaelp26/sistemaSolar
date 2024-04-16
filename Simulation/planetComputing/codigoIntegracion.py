import numpy as np
from planetComputing import tresPlanetas as p

def runge_kutta_integration(X, h, N, m1, m2, m3, m4, m5, m6):
    p1 = np.zeros((N, 2))
    p2 = np.zeros((N, 2))
    p3 = np.zeros((N, 2))
    p4 = np.zeros((N, 2))
    p5 = np.zeros((N, 2)) 
    p6 = np.zeros((N, 2))

    # Inicializa las posiciones del quinto planeta


    for k in range(N):
    
        K1 = p.tres_planetas(X, m1, m2, m3, m4,m5 ,m6)
        K2 = p.tres_planetas(X + 0.5 * h * K1, m1, m2, m3, m4 ,m5, m6)
        K3 = p.tres_planetas(X + 0.5 * h * K2, m1, m2, m3, m4 ,m5, m6)
        K4 = p.tres_planetas(X + 1.0 * h * K3, m1, m2, m3, m4 ,m5, m6)

        X = X + (1/6) * h * (K1 + 2 * K2 + 2 * K3 + K4)

        # Asigna las posiciones de cada planeta en cada paso de tiempo
        p1[k, 0], p1[k, 1] = X[0], X[1]
        p2[k, 0], p2[k, 1] = X[2], X[3]
        p3[k, 0], p3[k, 1] = X[4], X[5]
        p4[k, 0], p4[k, 1] = X[6], X[7]
        p5[k, 0], p5[k, 1] = X[8], X[9]
        p6[k, 0], p6[k, 1] = X[10], X[11]
        # Asigna las posiciones del quinto 
        
        

    return p1, p2, p3, p4, p5, p6,N  # Devuelve las posiciones de todos los planetas
  