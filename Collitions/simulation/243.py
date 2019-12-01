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

disk.VX = 0.000000000000000000005 # 0.5
disk.VY = 0.000000000000000000005 # 0.3

NoPart = 100
colors = ['red', 'blue', 'green', 'yellow', 'pink', 'magenta', 'cyan', 'orange', 'purple']
radio = 0.1 # 0.05

wind = False
System = sy.System(window = wind)
for i in range(NoPart):
    # System.particles.append(disk.Disk(vx = random.uniform(0.1, 0.7), vy = random.uniform(0.1, 0.7), rad = radio, col = random.choice(colors), tag = str(i)))
    System.particles.append(disk.Disk(vx = disk.VX, vy = disk.VY, rad = radio, col = random.choice(colors), tag = str(i)))

System.set_random_positions()

TempAA = 500
System.aux(TempAA)

cont = 0
for j in System.particles:
    # print(j)
    cont += 1
    j.obj = Circle((j.x, j.y), j.rad, color = j.col)
    j.vx = disk.VX
    j.vy = disk.VY

sim_time = 20000000000000000000000
Ptot, TempTot = System.main_loop(sim_time) # Retorna el Momentum en un tiempo t

print(TempTot)

# print(Ptot)
# print(System.Ptot())
# System.temperatura()

fig, ax = plt.subplots()
time = [i for i in range(0, len(TempTot))]
ax.plot(time, TempTot)
ax.set(xlabel = 't (tiempo)', ylabel = 'T(t) (Temperatura)(K°)', title = 'Temperatura Particle Collitions')
ax.grid()
plt.savefig("243TempTot.PNG")
plt.show()

################################################################################

# Tomando N = 100
# rad = 0.1
# VX entre 0 & 0.00000000000000000001 para todos los discos
# VY entre 0 & 0.00000000000000000001 para todos los discos
# sim_time = 20000000000000000000000

# Foto sobre formula

# Teniendo en cuenta que el Momentum Lineal total no se conserva con exactitud,
# y como en la formula la Temperatura T(t) depende del Momentum lineal total,
# entonces es de esperarse que la Temperatura tampoco se conserve de forma exacta,
# sino que tienda a oscilar y converger sobre un valor. : 243TempTot.PNG

# El efecto de aumentar las velocidades de todos los discos a lo largo de un
# tiempo t por un factor, implica que el Momentum va a aumentar, y como consecuencia directa,
# la temperatura tiende a aumentar ya que depende del Momentum cuando se calcula.
