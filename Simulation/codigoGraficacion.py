import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update_plot(frame, p1, p2, p3, p4, line1, line2, line3, line4, scatter1, scatter2, scatter3, scatter4):
    line1.set_data(p1[:frame, 0], p1[:frame, 1])
    line2.set_data(p2[:frame, 0], p2[:frame, 1])
    line3.set_data(p3[:frame, 0], p3[:frame, 1])
    line4.set_data(p4[:frame, 0], p4[:frame, 1])
    scatter1.set_offsets(p1[frame, :])
    scatter2.set_offsets(p2[frame, :])
    scatter3.set_offsets(p3[frame, :])
    scatter4.set_offsets(p4[frame, :])
    return line1, line2, line3, line4, scatter1, scatter2, scatter3, scatter4

def plot_animation(p1, p2, p3, p4, N):
    fig, ax = plt.subplots()
    line1, = ax.plot(p1[0], p1[1], 'k', label='Ruta del planeta 1')
    line2, = ax.plot(p2[0], p2[1], 'b', label='Ruta del planeta 2')
    line3, = ax.plot(p3[0], p3[1], 'r', label='Ruta del planeta 3')
    line4, = ax.plot(p4[0], p4[1], 'g', label='Ruta del planeta 4') 
    scatter1 = ax.scatter(p1[0], p1[1], c='k', marker='o', label='planeta 1')
    scatter2 = ax.scatter(p2[0], p2[1], c='b', marker='o', label='planeta 2')
    scatter3 = ax.scatter(p3[0], p3[1], c='r', marker='o', label='planeta 3')
    scatter4 = ax.scatter(p4[0], p4[1], c='g', marker='o', label='planeta 4')

    ax.grid(True)
    ax.set(xlim=[-0.2, 0.2], ylim=[-0.2, 0.2],
        xlabel='Distance [x]', ylabel='Distance [y]')
    ax.legend()
    ani = FuncAnimation(fig=fig, func=update_plot, frames=N, fargs=(
        p1, p2, p3, p4, line1, line2, line3, line4, scatter1, scatter2, scatter3, scatter4), interval=30, blit=True)

    plt.show()