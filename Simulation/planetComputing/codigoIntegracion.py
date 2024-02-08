import numpy as np
from planetComputing import dosPlanetas as p


def runge_kutta_integration(X, h, N, m1, m2):
    p1 = np.zeros((N, 2))
    p2 = np.zeros((N, 2))

    for k in range(N):
        K1 = p.dos_planetas(X, m1, m2)
        K2 = p.dos_planetas(X + 0.5 * h * K1, m1, m2)
        K3 = p.dos_planetas(X + 0.5 * h * K2, m1, m2)
        K4 = p.dos_planetas(X + 1.0 * h * K3, m1, m2)

        X = X + (1/6) * h * (K1 + 2 * K2 + 2 * K3 + K4)

        p1[k, 0], p1[k, 1] = X[0], X[1]
        p2[k, 0], p2[k, 1] = X[2], X[3]

    return p1, p2, N