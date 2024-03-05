import numpy as np

def tres_planetas(X, m1, m2, m3,m4):
    XP = np.zeros(16)
    G = 6.672e-11
    
    XP[0:8] = X[8:16]

    for i in range(4):
        for j in range(i+1, 4):
            dx = X[i*2] - X[j*2]
            dy = X[i*2 + 1] - X[j*2 + 1]
            rij = np.sqrt(dx**2 + dy**2) + 1e-9
            rij_cube = rij ** 3
            
            F = G * (m1 * m2 / rij_cube) if i == 0 and j == 1 else G * (m1 * m3 / rij_cube) if i == 0 and j == 2 else G * (m1 * m4 / rij_cube) if i == 0 and j == 3 else \
                G * (m2 * m3 / rij_cube) if i == 1 and j == 2 else G * (m2 * m4 / rij_cube) if i == 1 and j == 3 else \
                G * (m3 * m4 / rij_cube)

            XP[i*2 + 6] += F * dx
            XP[i*2 + 7] += F * dy
            XP[j*2 + 6] -= F * dx
            XP[j*2 + 7] -= F * dy

    return XP