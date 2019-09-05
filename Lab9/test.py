import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider, Button, RadioButtons


fig = plt.figure()
plt.subplots_adjust(bottom=0.25)

h0=0

ax2 = fig.add_subplot(111, projection='3d')

ax2.plot([1,1],[1,1],[0,1])

axhauteur = plt.axes([0.2, 0.1, 0.65, 0.03])
shauteur = Slider(axhauteur, 'Hauteur', 0.5, 10.0, valinit=h0)

def update(val):
    h = shauteur.val
    ax2.clear()
    ax2.plot([1, 1, 54, 8],[1, 1, 2, 5],[0, h, 7, 2])
    ax2.set_zlim(0, 10)
    fig.canvas.draw_idle()
shauteur.on_changed(update)
ax2.set_zlim(0,10)

plt.show()