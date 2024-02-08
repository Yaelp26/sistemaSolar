import numpy as np

def dos_planetas(X, m1, m2):
    XP = np.zeros(8)
    G = 6.672e-11
    
    XP[0:4] = X[4:8]

    L = np.sqrt((X[2] - X[0])**2 + (X[3] - X[1])**2) + 1e-9

    XP[4] = (G * m2 * (X[2] - X[0])) / (L**3)
    XP[5] = (G * m2 * (X[3] - X[1])) / (L**3)
    XP[6] = (G * m1 * (X[0] - X[2])) / (L**3)
    XP[7] = (G * m1 * (X[1] - X[3])) / (L**3)

    return XP
