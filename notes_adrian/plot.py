import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

scalar_factor = 1

frames = 500
cars = 3
v_max = 0.0333 * scalar_factor  # km/s = 120km/h
car_l = 0.0045 * scalar_factor  # km = 4.5m
update_time = 0.1  # s
dist = car_l * 3 * scalar_factor
p_max = 1/car_l

# use 1km
fig, ax = plt.subplots(1, 1)
fig.set_size_inches(15, 2)

# make equilibrium
x_front = [(0.1 - t * dist, 0.5) for t in range(cars)]
x_back = [(x_front[i][0] - car_l, x_front[i][1]) for i in range(cars)]

#TODO
def velocity(car_i):
    if car_i <= 0:
        raise Exception("first car has different velocity calculation")
    return v_max * np.log(p_max*abs(p_max*(x_front[car_i][0]-x_back[car_i-1][0])))


def move(car_i, v):
    x_front[car_i] = (x_front[car_i][0] + (v * update_time), x_front[car_i][1])
    
    #so car dont crash
    if car_i >0 and x_front[car_i][0] > x_back[car_i-1][0]:
        x_front[car_i] = x_back[car_i-1]
        
    x_back[car_i] = np.subtract(x_front[car_i], (car_l, 0))


def animate(i):
    ax.clear()

    for car_i in range(cars):
        if car_i ==0:
            move(car_i, v_max)
            ax.plot(*x_back[car_i], color="red", label="original", marker="o")
            ax.plot(*x_front[car_i], color="green", label="original", marker="o")
        else:
            move(car_i, v_max)
            #move(car_i, velocity(car_i))
            ax.plot(*x_back[car_i], color="red", label="original", marker="o")
            ax.plot(*x_front[car_i], color="black", label="original", marker="o")

    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])


ani = FuncAnimation(fig, animate, interval=update_time * 1000, repeat=False)

plt.show()
plt.close()
