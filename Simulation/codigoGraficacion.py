import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update_plot(frame, p1, p2, line1, line2, scatter1, scatter2):
    line1.set_data(p1[:frame, 0], p1[:frame, 1])
    line2.set_data(p2[:frame, 0], p2[:frame, 1])
    scatter1.set_offsets(p1[frame, :])
    scatter2.set_offsets(p2[frame, :])
    return line1, line2, scatter1, scatter2


def plot_animation( p1, p2, N):
    fig, ax = plt.subplots()
    line1, = ax.plot(p1[0], p2[0], 'k', label='Ruta del planeta 1')
    line2, = ax.plot(p1[0], p2[0], 'b', label='Ruta del planeta 2')
    scatter1 = ax.scatter(p1[0], p2[0], c='k', marker='o', label='planeta 1')
    scatter2 = ax.scatter(p1[0], p2[0], c='b', marker='o', label='planeta 2')

    ax.grid(True)
    ax.set(xlim=[-0.2, 0.2], ylim=[-0.2, 0.2],
           xlabel='Distance [x]', ylabel='Distance [y]')
    ax.legend()
    ani = FuncAnimation(fig=fig, func=update_plot, frames=N, fargs=(
        p1, p2, line1, line2, scatter1, scatter2), interval=30, blit=True)

    plt.show()

