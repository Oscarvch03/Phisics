# disk.py

################################################################################
# LIBRERIAS IMPORTADAS #########################################################

import numpy as np
from matplotlib.patches import Circle

################################################################################
# DEFINICION DE CLASES Y VARIABLES BLOBALES ####################################
WX, WY = 20, 20
LX, LY = 200, 200

VX = 0.5
VY = 0.3

class Disk:

    def __init__(self, x = None, y = None, vx = None, vy = None, mass = 1, rad = 1,
                 col = None, tag = -1):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        if vx and vy != None:
            self.v = np.sqrt(vx**2 + vy**2)
        self.mass = mass
        self.rad = rad
        self.col = col
        self.tag = tag
        self.wall_colls = 0
        self.disk_colls = 0
        self.obj = None


    def __str__(self):
        print()
        msg = "Tag = {0}\n".format(self.tag)
        msg += "r = ({0}, {1})\n".format(self.x, self.y)
        msg += "v = ({0}, {1})\n".format(self.vx, self.vy)
        msg += "col = {0}\n".format(self.col)
        msg += "mass = {0}, rad = {1}".format(self.mass, self.rad)
        return msg

    def num_colls(self):
        return self.wall_colls + self.disk_colls

    def horz_wall_coll(self):
        if self.vy < 0:
            return (self.rad - self.y) / self.vy
        elif self.vy > 0:
            return (LY - self.rad - self.y) / self.vy
        else:
            return np.inf

    def vert_wall_coll(self):
        if self.vx < 0:
            return (self.rad - self.x) / self.vx
        elif self.vx > 0:
            return (LX - self.rad - self.x) / self.vx
        else:
            return np.inf

    def disk_coll(self, other):
        if self is other:
            return np.inf

        dx = other.x - self.x
        dy = other.y - self.y
        dvx = other.vx - self.vx
        dvy = other.vy - self.vy

        dvdr = dx * dvx + dy * dvy

        if dvdr > 0:
            return np.inf

        dvdv = dvx * dvx + dvy * dvy

        if dvdv == 0:
            return np.inf

        drdr = dx * dx + dy * dy
        sigma = other.rad + self.rad
        d = (dvdr * dvdr) - dvdv * (drdr - sigma * sigma)

        if d < 0:
            return np.inf

        return -((dvdr + np.sqrt(d)) / dvdv)

    def move(self, time):
        self.x = self.x + self.vx * time
        self.y = self.y + self.vy * time

    def update_velocity_horz(self):
        self.vy = -self.vy
        self.wall_colls += 1

    def update_velocity_vert(self):
        self.vx = -self.vx
        self.wall_colls += 1

    def update_velocity_disk(self, other):
        Rij = (self.x - other.x, self.y - other.y)
        Vij = (self.vx - other.vx, self.vy - other.vy)

        Rji = (other.x - self.x, other.y - self.y)
        # Vji = (other.vx - self.vx, other.vy - self.vy)

        Ci = (2*self.mass) / (self.mass + other.mass)
        Cj = (2*other.mass) / (self.mass + other.mass)

        VijRij = (Vij[0]*Rij[0]) + (Vij[1]*Rij[1])

        Kj = -(Cj / ((self.rad + other.rad)**2))
        Ki = -(Ci / ((self.rad + other.rad)**2))

        Vi2x = (Kj*VijRij*Rij[0]) + self.vx
        Vi2y = (Kj*VijRij*Rij[1]) + self.vy

        Vj2x = (Ki*VijRij*Rji[0]) + other.vx
        Vj2y = (Ki*VijRij*Rji[1]) + other.vy

        self.vx = Vi2x
        self.vy = Vi2y
        other.vx = Vj2x
        other.vy = Vj2y

        self.disk_colls += 1
        other.disk_colls += 1

    def position(self, pos = None):
        if pos == None:
            return self.x, self.y
        else:
            self.x = pos[0]
            self.y = pos[1]

    def velocity(self, vel = None):
        if pos == None:
            return self.vx, self.vy
        else:
            self.vx = pos[0]
            self.vy = pos[1]

    def speed(self):
        return np.sqrt(self.vx**2 + self.vy**2)


################################################################################
# BLOQUE PRINCIPAL DE INSTRUCCIONES ############################################
