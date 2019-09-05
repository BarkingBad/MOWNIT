import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D
import pygsl.odeiv as odeiv


fig = plt.figure()
plt.subplots_adjust(bottom=0.2)

def lorenz(a = 10.0, b = 8.0 / 3.0, c = 28.0):

    def func(t, y, t2):
        f = np.zeros(3)
        f[0] = a * (y[1] - y[0])
        f[1] = c * y[0] - y[1] - y[0] * y[2]
        f[2] = y[0] * y[1] - b * y[2]
        return f

    dimension = 3
    step = odeiv.step_rk4(dimension, func)
    control = odeiv.control_y_new(step, 1e-6, 1e-6)
    evolve  = odeiv.evolve(step, control, dimension)
    h = 1
    t = 0.0
    t1 = 100.0
    y = (1.0, 1.0, 1.0)
    t, h, y = evolve.apply(t, t1, h, y)
    states = np.array([y[0], y[1], y[2]])

    while t<t1:
        t, h, y = evolve.apply(t, t1, h, y)
        states = np.vstack((states, np.array([y[0], y[1], y[2]])))

    return states


ax = fig.add_subplot(111, projection='3d')
states = lorenz()
ax.plot(states[:, 0], states[:, 1], states[:, 2])

a_slider = Slider(plt.axes([0.25, 0.20, 0.65, 0.03]), 'a', 0.1, 50.0, valinit=10.0)
b_slider = Slider(plt.axes([0.25, 0.15, 0.65, 0.03]), 'b', 0.1, 50.0, valinit=8.0/3.0)
c_slider = Slider(plt.axes([0.25, 0.10, 0.65, 0.03]), 'c', 0.1, 50.0, valinit=28.0)



def update(val):
    a = a_slider.val
    b = b_slider.val
    c = c_slider.val
    ax.clear()
    states = lorenz(a, b, c)
    ax.plot(states[:, 0], states[:, 1], states[:, 2])
    fig.canvas.draw_idle()


a_slider.on_changed(update)
b_slider.on_changed(update)
c_slider.on_changed(update)

plt.show()