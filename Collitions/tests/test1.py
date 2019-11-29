# test1.py

import sys
sys.path.insert(0, '../')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import random

import disk.disk as disk
import event.event as ev
import system.system as sy

# import matplotlib.animation as anim

disk.VX = 0.5
disk.VY = 0.5

NoPart = 10
colors = ['red', 'blue', 'green', 'yellow', 'pink', 'magenta', 'cyan', 'orange', 'purple']

wind = False
System = sy.System(window = wind)
for i in range(NoPart):
    System.particles.append(disk.Disk(vx = disk.VX, vy = disk.VY, rad = 2, col = random.choice(colors), tag = str(i)))

System.set_random_positions()

# check_overlap() # Revisar 2.4.1
System.check_overlap()

cont = 0
for j in System.particles:
    # print(j)
    cont += 1
    j.obj = Circle((j.x, j.y), j.rad, color = j.col)


# Grafica del Momentum
fig, ax = plt.subplots()


sim_time = 200000
Ptot = System.main_loop(sim_time)

# 2.4.1 Grafica del Momentum Lineal
# print(Ptot)
# print("len =", len(Ptot))
time = [i for i in range(0, len(Ptot))]
ax.plot(time, Ptot)
ax.grid()
plt.show()




################################################################################
# ANIMACION with matplotlib.animation
# fig2, ax2 = plt.subplots()
# fig2.set_size_inches(20, 20)
# fig2.patch.set_facecolor('xkcd:salmon')
#
# ax2.set_facecolor('xkcd:black')
# ax2.set_aspect('equal')
# ax2.set_xlim(0, 200)
# ax2.set_ylim(0, 200)
# ax2.set_title('Simulation Collition Particles')
# plt.grid(True, color = 'w')
#
# ball, = plt.plot(x[0], y[0], 'ro')
#
# def animate(i):
#     ball.set_data(x[i], y[i])
#     return ball,
#
# myAnimation = anim.FuncAnimation(fig2, animate, frames = np.arange(0, len(x), 1), blit = True, repeat = True)
#
# plt.show()
