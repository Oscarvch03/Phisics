# test1.py

import sys
sys.path.insert(0, '../')

import numpy as np
import disk.disk as disk
import event.event as ev
import system.system as sy

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


NoPart = 50

System = sy.System()

for i in range(1, NoPart + 1):
    System.particles.append(disk.Disk(x = 0, y = 0, col = 'red', tag = str(i)))

System.set_random_positions()

print(len(System.particles))
print()
cont = 0
for j in System.particles:
    # print(cont, j)
    cont += 1

fig, ax = plt.subplots(figsize = (disk.LX, disk.LY))
fig.patch.set_facecolor('xkcd:lightgreen')
ax.set_facecolor('xkcd:black')
ax.set_aspect('equal')
ax.set_xlim(0, 200)
ax.set_ylim(0, 200)

print(System.particles[0].obj)

circ = Circle((100, 100), 3, color = 'red')
# print("hola", circ)
# ax.add_artist(circ)

print(type(System.particles[0]))

ax.add_artist(System.particles[0].obj)
fig.canvas.draw()

ax.set_title('Simulation Collition Particles')
plt.grid(True, color = 'w')

# for k in System.particles:
#     ax.add_artist(k.obj)
#     fig.canvas.draw()



# fig.canvas.mpl_connect('button_press_event', animar)

plt.show()
