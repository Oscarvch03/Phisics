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

# 2.4.1 DEPURACION DE LA IMPLEMENTACIÓN
def check_overlap():
    for i in System.particles:
        for j in System.particles:
            if i.tag != j.tag:
                dist1 = np.sqrt((j.x - i.x)**2 + (j.y - i.y)**2)
                dist2 = i.rad + j.rad
                if dist1 < dist2:
                    print("2.4.1 check_overlap: Hay Overlap, Pailas.")
                    return
    print("2.4.1 check_overlap: Todo está Perfecto.")





NoPart = 50
colors = ['red', 'blue', 'green', 'yellow', 'pink']

wind = False
System = sy.System(window = wind)

for i in range(NoPart):
    System.particles.append(disk.Disk(vx = disk.VX, vy = disk.VY, rad = 3, col = random.choice(colors), tag = str(i)))

System.set_random_positions()

check_overlap() # Revisar 2.4.1

cont = 0
for j in System.particles:
    # print(j)
    cont += 1
    j.obj = Circle((j.x, j.y), j.rad, color = j.col)

sim_time = 1000
# x, y = System.main_loop(sim_time) # Revisar mejor fluidez para la ANIMACION
# System.main_loop(sim_time)
Ptot = System.main_loop(sim_time)
print(Ptot)

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


################################################################################
