# system.py

################################################################################
# LIBRERIAS IMPORTADAS #########################################################

import sys
sys.path.insert(0, '../')

import heapq as pq
import matplotlib.pyplot as plt

import numpy as np
import disk.disk as disk
import event.event as ev


################################################################################
# DEFINICION DE CLASES Y FUNCIONES

class System:
    def __init__(self, particles = [], window = None, fpe = None):
    	self.time = 0
    	self.minpq = []
    	self.particles = particles
    	self.turtles = []
    	self.frame, self.fpe = 0, fpe
    	self.window = window


    def __str__(self):
    	pal = "System: {} particles\n".format(len(self.particles))
    	pal += "t = {:2f}\n".format(self.time)
    	pal += "\n".join(map(str, self.particles)) + "\n"
    	pal += "Collision priority queue: {}\n".format(len(self.minpq))
    	pal += "| " + " | ".join(map(repr, self.minpq)) + " |"
    	return pal


    def check_colls(self, saucer, sim_time):

        for dish in self.particles:
            t_disk = saucer.disk_coll(dish)
            if self.time + t_disk <= sim_time:
                event = ev.Event(self.time + t_disk, saucer, dish)
                pq.heappush(self.minpq, event)

        t_vert = saucer.vert_wall_coll()
        t_horz = saucer.horz_wall_coll()

        if self.time + t_vert <= sim_time:
            event = ev.Event(self.time + t_vert, saucer, None)
            pq.heappush(self.minpq, event)
        if self.time + t_horz <= sim_time:
            event = ev.Event(self.time + t_horz, None, saucer)
            pq.heappush(self.minpq, event)


    def valid(self, event):
        this_tag, that_tag = event.this_tag, event.that_tag
        this_ocolls, that_ocolls = event.this_colls, event.that_colls
        if this_tag is not None:
            this_ncolls = self.particles[int(this_tag)].num_colls()
            if this_ncolls > this_ocolls:
                return False
        if that_tag is not None:
            that_ncolls = self.particles[int(that_tag)].num_colls()
            if that_ncolls > that_ocolls:
                return False
        return True


    def next_valid_event(self):

        while self.minpq != []:
            event = pq.heappop(self.minpq)
            if self.valid(event):
                return event
        return None


    def move_all_particles(self, event):
        event_time = event.time
        for dish in self.particles:
            dish.move(event_time - self.time)
        self.time = event.time


    def update_velocities(self, event):
        tag_a, tag_b = event.this_tag, event.that_tag

        if tag_a is not None and tag_b is not None:
            self.particles[int(tag_a)].update_velocity_disk(self.particles[int(tag_b)])
        elif tag_a is not None and tag_b is None:
            self.particles[int(tag_a)].update_velocity_vert()
        elif tag_a is None and tag_b is not None:
            self.particles[int(tag_b)].update_velocity_horz()


    def predict_colls(self, event, sim_time):
        tag_a, tag_b = event.this_tag, event.that_tag

        if tag_a is not None:
            self.check_colls(self.particles[int(tag_a)], sim_time)

        if tag_b is not None:
            self.check_colls(self.particles[int(tag_b)], sim_time)


################################################################################
    # 2.4.1 DEPURACION DE LA IMPLEMENTACION

    def check_overlap(self):
        for i in self.particles:
            for j in self.particles:
                if i.tag != j.tag:
                    dist1 = np.sqrt((j.x - i.x)**2 + (j.y - i.y)**2)
                    dist2 = i.rad + j.rad
                    if dist1 < dist2:
                        print("2.4.1 check_overlap: Hay Overlap, Pailas.")
                        return
        print("2.4.1 check_overlap(): Todo está Perfecto.")


    def Ptot(self):
        p = 0
        N = len(self.particles)
        for i in range(0, N):
            part = self.particles[i]
            p += part.mass * part.speed()
        p /= N
        # print("      Ptot: Calculando Momentum y graficando.")
        return p

################################################################################

################################################################################
    # 2.4.2 RED RECTANGULAR Y DENSIDAD DE PARTICULAS

    def red_cuadrada(self, f, c):
        df1 = disk.LX / c
        dc1 = disk.LY / f
        # print("df1 =", df1, "df2 =", df1)
        cont = 0
        dc2 = dc1 - self.particles[cont].rad
        for i in range(f):
            df2 = df1 - self.particles[cont].rad
            for j in range(c):
                self.particles[cont].x = df2 # round(df2, 2)
                self.particles[cont].y = dc2 # round(dc2, 2)
                df2 += df1 # round(df1, 2)
                cont += 1
            dc2 += dc1 # round(dc1, 2)

################################################################################
    def main_loop(self, sim_time, fpe=None):
        # Funcion bella & hermosa que hace todo
        Ptot = []
        if self.window == True:
            fig, ax = plt.subplots()
            fig.set_size_inches(disk.WX, disk.WY)
            fig.patch.set_facecolor('xkcd:lightgreen')

            ax.set_facecolor('xkcd:black')
            ax.set_aspect('equal')
            ax.set_xlim(0, disk.LX)
            ax.set_ylim(0, disk.LY)
            ax.set_title('Simulation Collition Particles')
            plt.grid(True, color = 'w')

        for dish in self.particles:
            self.check_colls(dish, sim_time)
            if self.window == True:
                ax.add_artist(dish.obj)
        if self.window == True:
            fig.canvas.draw()
            plt.pause(3)

        cont = 0
        while(len(self.minpq) != 0):
            event = self.next_valid_event()
            if event is None:
                break
            self.move_all_particles(event)
            self.update_velocities(event)
            self.predict_colls(event, sim_time)
            cont += 1

            for k in self.particles:
                k.obj.center = k.x, k.y
            if self.window == True:
                fig.canvas.draw()
                plt.pause(0.000000000000001)

            Pt = self.Ptot()
            Ptot.append(round(Pt, 2))

        if self.window == True:
            plt.show()

        print("      Ptot(): Calculando Momentum y graficando.")

        return Ptot


    ############################################
    # def write_time_to_screen(self)
    # def create_all_artists(self)
    # def draw_all_artists(self)
    ############################################


    def set_random_positions(self):
        self.particles[0].x = disk.LX/2.0
        self.particles[0].y = disk.LY/2.0

        for idx, idish in enumerate(self.particles[1:], start = 1):
            irad, overlap = idish.rad, True

            while overlap:
                jdx, overlap = 0, False
                dicex = (disk.LX - 2.0 * irad) * np.random.random() + irad
                dicey = (disk.LY - 2.0 * irad) * np.random.random() + irad
                tmp_pos = np.array([dicex, dicey])

                while jdx < idx and not overlap:
                    jdish = self.particles[jdx]
                    jstate = np.array([jdish.x, jdish.y])
                    metric = np.linalg.norm(tmp_pos - jstate[:2])

                    if metric <= irad + jdish.rad:
                        overlap = True
                    jdx += 1

                idish.x = tmp_pos[0]
                idish.y = tmp_pos[1]
