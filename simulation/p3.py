# p3.py

################################################################################
# LIBRERIAS IMPORTADAS Y VARIABLES GLOBALES

import sys
sys.path.insert(0, '../')

import numpy as np
import matplotlib.pyplot as plt

import particle.particle as pt
import solver.solver as sl
import forces.forces as fr

GM = 4 * (np.pi)**2


################################################################################
# DEFINICION DE CLASES Y FUNCIONES

def universal_gravity(state, params):
    x, y, vx, vy, _ = state
    mass, gu = params
    r2 = x**2 + y**2
    r3 = np.sqrt(r2) * r2
    ax = -gu * x / r3
    ay = -gu * y / r3
    return vx, vy, ax, ay, 1.


################################################################################
# BLOQUE PRINCIPAL DE INSTRUCCIONES
x0 = 1.1
vy0 = 1.1

v0 = vy0
x0, y0, v0, a0, m = x0, .0, v0, 90., 1.
sim_params = m, GM
deltat = 0.01/1024

m1 = "Euler"
m2 = "Euler-Cromer"
m3 = "Midpoint"

earth = pt.Particle("Earth", x0, y0, v0, a0, m)
print(earth)
earth_force = fr.Forces(universal_gravity, sim_params)
earth.set_force(earth_force)
euler = sl.Solver(earth, m2, deltat)
xpos, ypos, tpos = [], [], []
vpos = []
cont = 0

for i in range(200000):
    xc, yc, vxc, vyc, tc = earth.get_state()
    # if tc > 0.415:
    #     break
    v = np.sqrt(vxc**2 + vyc**2)
    vpos.append(v)
    xpos.append(xc)
    ypos.append(yc)
    tpos.append(tc)
    euler.do_step()
    xc1, yc1, vxc1, vyc1, tc1 = earth.get_state()
    if yc < 0 and yc1 >= 0:
        cont += 1

vmin = min(vpos)
tmin = tpos[vpos.index(vmin)]
vmax = max(vpos)
tmax = tpos[vpos.index(vmax)]

print("Vmin:", vmin, ", with t = ", tmin)
print("Vmax:", vmax, ", with t = ", tmax)

print("Orbitas:", cont)
# print(tpos)

fig, ax = plt.subplots()
ax.plot(xpos, ypos, '--', label=m2)

ax.set(xlabel='x (a.u.)', ylabel='y (a.u.)',
       title='Simulation Planet Motion, deltat: ' + str(deltat))



# fig, ax = plt.subplots()
# ax.plot(tpos, vpos, '--', label=m2)
#
# ax.set(xlabel='t (yr)', ylabel="v (a.u./yr)",
#        title='Simulation Planet Motion, deltat: ' + str(deltat))


ax.grid()
plt.legend()
plt.show()


# Con deltat = 0.01/1024, y0 = 0, vx0 = 0
# 1) x0 = 1, vy0 = 1
# 2) x0 = 1.1, vy0 = 1.1
# 3) x0 = 1.2, vy0 = 1.2
# 4) x0 = 1.3, vy0 = 1.3
# 5) x0 = 1.4, vy0 = 1.4
# 6) x0 = 1.5, vy0 = 1.5
# 7) x0 = 1.6, vy0 = 1.6
# 8) x0 = 1.7, vy0 = 1.7
# 9) x0 = 1.8, vy0 = 1.8
# 10) x0 = 1.9, vy0 = 1.9
# Hay trayectorias elipticas
