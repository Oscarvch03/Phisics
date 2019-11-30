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

disk.VX = 0.9
disk.VY = 0.9

NoPart = 50
colors = ['red', 'blue', 'green', 'yellow', 'pink', 'magenta', 'cyan', 'orange', 'purple']
radio = 2

wind = False
System = sy.System(window = wind)

#-------DISTINTAS VELOCIDADES PARA LOS DISCOS----------
factor_constante = 1
for i in range(NoPart):
    disk.VX = random.uniform(0.1, 3) * factor_constante
    disk.VY = random.uniform(0.1, 3) * factor_constante
    System.particles.append(disk.Disk(vx = disk.VX, vy = disk.VY, rad = radio, col = random.choice(colors), tag = str(i)))

System.set_random_positions()

# 2.4.3 Temperatura()
temperatura = 0
for k in System.particles:
    mi = k.mass/2
    vi = k.vx * k.vx + k.vy + k.vy
    temperatura += mi*vi/(NoPart)

print(temperatura)
#------------DISTINTAS VELOCIDADES DADAS-----------------
vels = []
temperatura = 0
for k in System.particles:
    mi = k.mass/2
    vi = k.vx * k.vx + k.vy + k.vy
    temperatura += mi*vi/(NoPart)

print(temperatura)


cont = 0
for j in System.particles:
    # print(j)
    cont += 1
    j.obj = Circle((j.x, j.y), j.rad, color = j.col)

sim_time = 200000
Ptot = System.main_loop(sim_time) # Retorna el Momentum en un tiempo t

# 2.4.1 Grafica del Momentum Lineal
# print(Ptot)
# print("len =", len(Ptot))
fig, ax = plt.subplots()
time = [i for i in range(0, len(Ptot))]
ax.plot(time, Ptot)
ax.set(xlabel = 't (tiempo)', ylabel = 'Ptot(t) (Momentum)', title = 'Momentum Particle Collitions')
ax.grid()
# plt.savefig("241Ptot.PNG")
plt.show()
