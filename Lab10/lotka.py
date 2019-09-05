import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from PIL import Image
import random
from time import sleep
import threading

fig = plt.figure()
plt.axis('off')
plt.subplots_adjust(bottom=0.2)



ax = fig.add_subplot(111)

size = 128
states = [[0 for x in range(size)] for y in range(size)] 
ages = [[0 for x in range(size)] for y in range(size)] 
stop_thread = False

img = Image.new( 'RGB', (size*4, size*4), "black")
pixels = img.load()
ax.imshow(img)

def random_state(rabbits_population, wolves_population):
    chances = random.uniform(0, 1)
    if chances < wolves_population:
        return 2
    elif chances < wolves_population + rabbits_population:
        return 3
    else:
        return 1

def setup(rabbits_population, wolves_population):
    for i in range(size):
        for j in range(size):
            states[i][j] = random_state(rabbits_population, wolves_population)
    pass

lock = threading.Lock()
def draw():
    while True:
        lock.acquire()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                state = states[int(i/4)][int(j/4)]
                pixels[i,j] = (215, 215, 215) if state == 1 else ((255, 0, 0) if state == 2 else (0, 0, 255))
        ax.clear()
        ax.axis('off')
        ax.imshow(img)
        fig.canvas.draw_idle()
        print("rysuje")
        lock.release()
        sleep(0.01)

safe_range = [x for x in range(size)]

directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
def show():
    age=0
    while True:
        lock.acquire()
        print(age, stop_thread)
        for i in range(size):
            for j in range(size):
                if ages[i][j] > age:
                    continue

                state = states[i][j]

                if state == 1:
                    ages[i][j] = age + 1
                    continue

                adjacent = {1: [], 2: [], 3: []}

                for dir in directions:
                    x, y = dir
                    if i+x in safe_range and j+y in safe_range:
                        adjacent[states[i+x][j+y]] += [(i+x, j+y)]

                if state == 2:
                    if not adjacent[3]:
                        states[i][j] = 1
                        continue
                    prex, prey = random.choice(adjacent[3]) 
                    states[prex][prey] = 2
                    ages[prex][prey] = age + 1

                    if adjacent[1]:
                        prex, prey = random.choice(adjacent[1])
                        states[i][j] = 1
                        states[prex][prey] = 2
                        ages[prex][prey] = age + 1

                if state == 3:
                    if adjacent[1]:
                        prex, prey = random.choice(adjacent[1])
                        states[prex][prey] = 3
                        ages[prex][prey] = age + 1

                ages[i][j] = age + 1
        lock.release()
        age = age + 1
        sleep(0.01)


rabbit_slider = Slider(plt.axes([0.25, 0.15, 0.65, 0.03]), 'Rabbits starting population', 0.0, 1.0, valinit=0.2)
wolf_slider = Slider(plt.axes([0.25, 0.10, 0.65, 0.03]), 'Wolves starting population', 0.0, 1.0, valinit=0.05)
start_button = Button(plt.axes([0.10, 0.05, 0.1, 0.03]), 'Start')

setup(0.2, 0.05)
t1 = threading.Thread(target=show)
t2 = threading.Thread(target=draw)
t1.start()
t2.start()

def update(val):
    rabbits_population = rabbit_slider.val
    wolves_population = wolf_slider.val
    ax.clear()
    ax.axis('off')
    lock.acquire()
    setup(rabbits_population, wolves_population)
    lock.release()




start_button.on_clicked(update)

plt.show()
