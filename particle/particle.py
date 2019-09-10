import numpy as np

GRAV = 9.8

class Particle:

    def __init__(self, label, x0, y0, v0, a0, m0 = 1., t0 = 0.):
        self.label = label
        self.x = x0
        self.y = y0
        self.vx = v0 * np.cos(np.radians(a0))
        self.vy = v0 * np.sin(np.radians(a0))
        self.mass = m0
        self.time = t0

    def __str__(self):

        msg = "Particle: {} \nmass = {:.4f}, t = {:.4f} \n".format(self.label,
                                                                   self.mass,
                                                                   self.time)
        msg += "r = ({:.4f}, {:.4f}) \nv = ({:.4f}, {:.4f})".format(self.x,
                                                                    self.y,
                                                                    self.vx,
                                                                    self.vy)
        return msg

    def get_state(self):
        return self.x, self.y, self.vx, self.vy, self.time

    def step(self, dt):
        self.x = self.x + dt * self.vx
        self.y = self.y + dt * self.vy
        self.vx = self.vx
        self.vy = self.vy - dt * GRAV
        self.time += dt


if __name__ == "__main__":
    mars = Particle("Mars", 1., 2., 3., 4.)
    print(mars)
