################################################################################
# LIBRERIAS IMPORTADAS #########################################################

import sys
sys.path.insert(0, '../')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import random

import disk.disk as disk
import event.event as ev
import system.system as sy

################################################################################
# BLOQUE PRINCIPAL DE INSTRUCCIONES ############################################

disk.LX = 11
disk.LY = 11

disk.VX = 0.5
disk.VY = 0.3

NoPart = 100
colors = ['red', 'blue', 'green', 'yellow', 'pink', 'magenta', 'cyan', 'orange', 'purple']
radio = 0.3 # 0.05

wind = True
System = sy.System(window = wind)
for i in range(NoPart):
    # System.particles.append(disk.Disk(vx = random.uniform(0.1, 0.7), vy = random.uniform(0.1, 0.7), rad = radio, col = random.choice(colors), tag = str(i)))
    System.particles.append(disk.Disk(vx = disk.VX, vy = disk.VY, rad = radio, col = random.choice(colors), tag = str(i)))

System.red_cuadrada(10, 10)

cont = 0
for j in System.particles:
    # print(j)
    cont += 1
    j.obj = Circle((j.x, j.y), j.rad, color = j.col)

sim_time = 5000
Ptot = System.main_loop(sim_time) # Retorna el Momentum en un tiempo t
