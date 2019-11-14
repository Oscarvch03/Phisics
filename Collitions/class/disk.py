# disk.py

import numpy as np

LX, LY = 10, 8
VEL_SCALE = 0.9

class Disk:

    def __init__(self, x = None, y = None, vx = None, vy = None, mass = 1, rad = 1,
                 col = (0, 0, 0), tag = -1):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.v = np.sqrt(vx**2 + vy**2)
        self.mass = mass
        self.rad = rad
        self.col = col
        self. tag = tag
        self.wall_colls = 0
        self.disk_colls = 0


    def __str__(self):
        msg = "Tag = {0}\n".format(self.tag)
        msg += "r = ({0}, {1})\n".format(self.x, self.y)
        msg += "v = ({0}, {1})\n".format(self.vx, self.vy)
        msg += "col = {0}\n".format(self.col)
        msg += "mass = {0}, rad = {1}\n".format(self.mass, self.rad)
        return msg

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
