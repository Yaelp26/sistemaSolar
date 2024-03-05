import numpy as np
from planetComputing import tresPlanetas as p

def runge_kutta_integration(X, h, N, m1, m2, m3, m4):
    p1 = np.zeros((N, 2))
    p2 = np.zeros((N, 2))
    p3 = np.zeros((N, 2))
    p4 = np.zeros((N, 2))

    for k in range(N):
        K1 = p.tres_planetas(X, m1, m2, m3, m4)
        K2 = p.tres_planetas(X + 0.5 * h * K1, m1, m2, m3, m4)
        K3 = p.tres_planetas(X + 0.5 * h * K2, m1, m2, m3, m4)
        K4 = p.tres_planetas(X + 1.0 * h * K3, m1, m2, m3, m4)

        X = X + (1/6) * h * (K1 + 2 * K2 + 2 * K3 + K4)

        p1[k, 0], p1[k, 1] = X[0], X[1]
        p2[k, 0], p2[k, 1] = X[2], X[3]
        p3[k, 0], p3[k, 1] = X[4], X[5]
        p4[k, 0], p4[k, 1] = X[6], X[7]

    return p1, p2, p3, p4, N