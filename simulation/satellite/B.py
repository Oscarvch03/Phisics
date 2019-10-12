# A.py

################################################################################
# LIBRERIAS IMPORTADAS Y VARIABLES GLOBALES

import sys
sys.path.insert(0, '../../')

import numpy as np
import matplotlib.pyplot as plt

import particle.particle as pt
import solver.solver as sl
import forces.forces as fr

GMe = 20

W = 0. # con 0 <= A <= 0.3538, de 11 a 7 orbitas, luego se totea por errores numericos
print("Con W =", W)
