import sys
sys.path.insert(0, '../')

import numpy as np
import matplotlib.pyplot as plt

GM = 4 * (np.pi)**2

import particle.particle as pt
import solver.solver as sl
import forces.forces as fr

def cond_init(x, y, vx):
    v = np.sqrt((4 * (np.pi)**2) / (x**2 + y**2))
    # vy = np.sqrt(v**2 - vx**2)
    return float(v)

def universal_gravity(state, params):
    x, y, vx, vy, _ = state
    mass, gu = params
    r2 = x**2 + y**2
    r3 = np.sqrt(r2) * r2
    ax = -gu * x / r3
    ay = -gu * y / r3
    return vx, vy, ax, ay, 1.


v0 = cond_init(1, 0, 0)
x0, y0, v0, a0, m = 1., .0, v0, 90., 1.
sim_params = m, GM
deltat = 0.01/512

m1 = "Euler"
m2 = "Euler-Cromer"
m3 = "Midpoint"

earth = pt.Particle("Earth", x0, y0, v0, a0, m) # Revisar por que a0 es 90?
earth_force = fr.Forces(universal_gravity, sim_params)
earth.set_force(earth_force)
euler = sl.Solver(earth, m3, deltat) # ??? Euler & Euler-Cromer son iguales, y mas estables que midpoint
xpos, ypos, tpos = [], [], []
cont = 0

for i in range(200000):
    xc, yc, _, _, tc = earth.get_state()
    xpos.append(xc)
    ypos.append(yc)
    tpos.append(tc)
    euler.do_step()
    xc1, yc1, _, _, tc1 = earth.get_state()
    if yc < 0 and yc1 >= 0:
        cont += 1

print("Orbitas:", cont) # Aqui nos damos cuenta cuantas orbitas circulares hace el planeta

# print(tpos)
fig, ax = plt.subplots()
ax.plot(xpos, ypos, '--', label=m3)

ax.set(xlabel='x (a.u.)', ylabel='y (a.u.)',
       title='Projectile motion with drag')
ax.grid()

plt.legend()
plt.show()
