import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update_plot(frame, p1, p2, p3, p4, p5, p6,line1, line2, line3, line4,line5,line6, scatter1, scatter2, scatter3, scatter4,scatter5,scatter6):
    line1.set_data(p1[:frame, 0], p1[:frame, 1])
    line2.set_data(p2[:frame, 0], p2[:frame, 1])
    line3.set_data(p3[:frame, 0], p3[:frame, 1])
    line4.set_data(p4[:frame, 0], p4[:frame, 1])
    line5.set_data(p5[:frame, 0], p5[:frame, 1])
    line6.set_data(p6[:frame, 0], p6[:frame, 1])

    scatter1.set_offsets(p1[frame, :])
    scatter2.set_offsets(p2[frame, :])
    scatter3.set_offsets(p3[frame, :])
    scatter4.set_offsets(p4[frame, :])
    scatter5.set_offsets(p5[frame, :])
    scatter6.set_offsets(p6[frame, :])

    return line1, line2, line3, line4,line5,line6 , scatter1, scatter2, scatter3, scatter4,scatter5,scatter6

def plot_animation(p1, p2, p3, p4,p5, p6, N):
    fig, ax = plt.subplots()
    line1, = ax.plot(p1[0], p1[1], 'k', label='Ruta del planeta 1')
    line2, = ax.plot(p2[0], p2[1], 'b', label='Ruta del planeta 2')
    line3, = ax.plot(p3[0], p3[1], 'r', label='Ruta del planeta 3')
    line4, = ax.plot(p4[0], p4[1], 'g', label='Ruta del planeta 4') 
    line5, = ax.plot(p5[0], p5[1], 'y', label='Ruta del planeta 5')
    line6, = ax.plot(p6[0], p6[1], 'm', label='Ruta del planeta 6')

    scatter1 = ax.scatter(p1[0], p1[1], c='k', marker='o', label='sol')
    scatter2 = ax.scatter(p2[0], p2[1], c='b', marker='o', label='mercurio')
    scatter3 = ax.scatter(p3[0], p3[1], c='r', marker='o', label='venus')
    scatter4 = ax.scatter(p4[0], p4[1], c='g', marker='o', label='tierra')
    scatter5 = ax.scatter(p5[0], p5[1], c='y', marker='o', label='marte')
    scatter6 = ax.scatter(p6[0], p6[1], c='m', marker='o', label='jupiter')
    


    ax.grid(True)
    ax.set(xlim=[-10, 10], ylim=[-10, 10],
        xlabel='Distance [x]', ylabel='Distance [y]')
    ax.legend()
    ani = FuncAnimation(fig=fig, func=update_plot, frames=N, fargs=(p1, p2, p3, p4,p5,p6, line1, line2, line3, line4,line5,line6, scatter1, scatter2, scatter3, scatter4,scatter5,scatter6), interval=30, blit=True)

    plt.show()