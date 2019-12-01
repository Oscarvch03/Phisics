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
radio = 0.1 # 0.05

wind = True
System = sy.System(window = wind)
for i in range(NoPart):
    System.particles.append(disk.Disk(vx = random.uniform(0.1, 0.7), vy = random.uniform(0.1, 0.7), rad = radio, col = random.choice(colors), tag = str(i)))
    # System.particles.append(disk.Disk(vx = disk.VX, vy = disk.VY, rad = radio, col = random.choice(colors), tag = str(i)))

System.red_cuadrada(10, 10)

cont = 0
for j in System.particles:
    # print(j)
    cont += 1
    j.obj = Circle((j.x, j.y), j.rad, color = j.col)

sim_time = 20000
Ptot, TempTot = System.main_loop(sim_time) # Retorna el Momentum en un tiempo t
# plt.savefig("242redCI.PNG")
print(System.densidad())

################################################################################

# Tomando N = 100
# rad = 0.55, VX & VY cualesquiera para todos los discos, la densidad del sistema
# esta definida como n = N/(LX*LY), donde N es la cantidad de discos, y LX & LY
# son las dimensiones del contenedor de los discos.
# La densidad máxima del sistema es n = 100/(11*11) = 0.826446 y se da cuando
# tenemos 100 discos impenetrables de radio 0.55, ya que asi los 100 discos no
# se pueden mover al estar completamente encerrados: 242densidadmaxima.PNG

# Tomando N = 100
# VX = 0.5, VY = 0.3, rad = 0.1 para todos los discos

# Tenemos primeramente la red regular (cuadrada): 242redCI.PNG

# Después de muchas colisiones, cuando todos los discos tienen la misma velocidad,
# se observa un patron en las colisiones (equilibrio), chocan diagonalmente, en principio
# lo unico que cambia en los discos es que la direccion se vuelve opuesta, mas
# adelante como los muros si cambian la direccion de los discos cambia y asi se
# van generando choques entre discos mas aleatoriamente, cambiando tanto la
# magnitud como la direccion en la velocidad de los discos.
# Inicialmente todos los discos tienen entre 3 y 4 vecinos: 242redCI.PNG
# Luego de muchas colisiones la cantidad de vecinos está entre 3 & 8 pero ahora los
# discos están en movimiento: 242redCF.PNG


# Tomando N = 100
# rad = 0.1 para todos los discos
# velocidades aleatorias entre 0.1 & 0.7 para todos los discos

# Despues de muchas colisiones, cuando todos los discos tienen velocidades
# aleatorias da igual si se ubicaron inicialmente  en una red regular o no, porque
# todos los discos salen en direcciones "aleatorias" generando asi a lo largo del
# tiempo, siempre colisiones "aleatorias".
# Asi cada disco puede tener 0 vecinos, (estar aislado), o tener entre
# 1 a 8 vecinos mientras colisiona. : 242redCF2.PNG
