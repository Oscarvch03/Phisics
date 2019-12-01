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
for i in range(NoPart):
    System.particles.append(disk.Disk(vx = disk.VX, vy = disk.VY, rad = radio, col = random.choice(colors), tag = str(i)))

System.set_random_positions()

# 2.4.1 check_overlap()
System.check_overlap()

cont = 0
for j in System.particles:
    # print(j)
    cont += 1
    j.obj = Circle((j.x, j.y), j.rad, color = j.col)

sim_time = 20000
Ptot, TempTot = System.main_loop(sim_time) # Retorna el Momentum en un tiempo t

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

################################################################################

# Tomando N = 50
# VX = 0.9; VY = 0.9; rad = 2 para todos los discos
# sim_time = 20000

# Después de ejecutar la función check_overlap() podemos afirmar que los discos
# no se solapan, así podemos comenzar con la función mainloop() que se encarga de
# correr la simulación

# Además la idea es calcular el Momentum Lineal a medida que avanza el tiempo,
# asi que lo calculamos con la función Ptot(t) y posteriormente hacemos una
# grafica con toda la información recopilada: 241Ptot.PNG

# Como el Momentum Lineal es un vector, podemos separarlo en Momentum sobre el
# eje x y Momentum sobre el eje y: 241Ptotx.PNG & 241Ptoty.PNG

# Podemos concluir que el Momentum Lineal total no se conserva de forma exacta,
# lo cual se ve en las graficas, ya que los muros por asi decirlo tienen
# masa infinita, y como estos me afectan las colisiones, se generan cambios de
# velocidades que afectan el Momentum.
