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

disk.VX = 0.9
disk.VY = 0.9

NoPart = 50
colors = ['red', 'blue', 'green', 'yellow', 'pink', 'magenta', 'cyan', 'orange', 'purple']

wind = False
System = sy.System(window = wind)
for i in range(NoPart):
    System.particles.append(disk.Disk(vx = disk.VX, vy = disk.VY, rad = 2, col = random.choice(colors), tag = str(i)))
