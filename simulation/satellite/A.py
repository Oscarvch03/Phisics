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

A = 0.3538 # con 0 <= A <= 0.3538, de 11 a 7 orbitas, luego se totea por errores numericos
print("Con A =", A)


################################################################################
# DEFINICION DE CLASES Y FUNCIONES

def cond_init(x, y, vx):
    v = np.sqrt(GMe / np.sqrt(x**2 + y**2))
    vy = np.sqrt(v**2 - vx**2)
    return float(v), vy

def universal_gravity(state, params):
    x, y, vx, vy, _ = state
    mass, gu, A = params
    r2 = x**2 + y**2
    r3 = np.sqrt(r2) * r2
    ax = (-gu * x / r3) + A * np.sqrt(vx**2 + vy**2) * x
    ay = (-gu * y / r3) - A * np.sqrt(vx**2 + vy**2) * y
    return vx, vy, ax, ay, 1.

def total_mechanic_energy(v, m): # cambiar con A & W
    emt = (1/2) * m * (v**2) + GMe * m  # Julian nos la dio asi, hay que averiguar por que
    return emt


################################################################################
# BLOQUE PRINCIPAL DE INSTRUCCIONES

v0, vy = cond_init(1, 0, 0)
# print(v0)
x0, y0, v0, a0, m = 1., .0, v0, 90., 1.
sim_params = m, GMe, A
deltat = 0.01/128

m1 = "Euler"
m2 = "Euler-Cromer"
m3 = "Midpoint"

satellite = pt.Particle("Satellite", x0, y0, v0, a0, m) # Revisar por que a0 es 90?
satellite_force = fr.Forces(universal_gravity, sim_params)
satellite.set_force(satellite_force)
euler = sl.Solver(satellite, m2, deltat) # El metodo mas estable es Euler Cromer
xpos, ypos, tpos = [], [], []
cont = 0

em = []
vel = []
for i in range(200000):
    xc, yc, vxc, vyc, tc = satellite.get_state()
    v = np.sqrt(vxc**2 + vyc**2)
    vel.append(v)
    emt = total_mechanic_energy(v, m)
    em.append(round(emt, 2))
    xpos.append(xc)
    ypos.append(yc)
    tpos.append(tc)
    euler.do_step()
    xc1, yc1, vxc1, vyc1, tc1 = satellite.get_state()
    if yc < 0 and yc1 >= 0:
        cont += 1

print("Method:", m2, ", dt:", deltat)
# for j in em:
#     print("Energia Mec Tot:", j)
print("Energia Mec Tot In:", em[0], ", Energia Mec Tot Fin:", em[-1])
print("Orbitas:", cont)

# emmt = tpos[em.index(max(em))]
# # print(emmt)
# emmx = xpos[tpos.index(emmt)]
# emmy = ypos[tpos.index(emmt)]
# print("Punto donde emt es max:, x = ", round(emmx, 5), "& y =", round(emmy, 5))
# print("Con t =", round(emmt, 4), ", emtm =", max(em))


# fig, ax = plt.subplots()
# ax.plot(xpos, ypos, '--', label=m2)
#
# ax.set(xlabel='x (a.u.)', ylabel='y (a.u.)',
#        title='Projectile motion with drag, deltat: ' + str(deltat) + ', Orbits:' + str(cont))
# ax.grid()

# fig, ax = plt.subplots()
# ax.plot(tpos, em, '--', label=m2)
#
# ax.set(xlabel='t (yr)', ylabel='emt',
#        title='Simulation Planet Motion, deltat: ' + str(deltat) + ', Orbits:' + str(cont))
# ax.grid()

fig, ax = plt.subplots()
ax.plot(tpos, vel, '--', label=m2)

ax.set(xlabel='t (yr)', ylabel='v(E.U / h)',
       title='Simulation Planet Motion, deltat: ' + str(deltat) + ', Orbits:' + str(cont))
ax.grid()

plt.legend()
# plt.savefig("p1Midpoint.jpg")
plt.show()
