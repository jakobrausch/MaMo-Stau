import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames=500
cars=3

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(10,2)
x_start=[(0.1-t*0.05,0.5) for t in range(cars)]


def move(x_start, time):
    return (x_start[0]+time/frames, x_start[1])

def animate(i):
    ax.clear()
    for car_i in range(cars):
        ax.plot(*move(x_start[car_i],i), color='green', label='original', marker='o')

    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
ani = FuncAnimation(fig, animate, frames = frames,
                    interval=50, repeat=False)
plt.show()
plt.close()
