# system.py

import sys
sys.path.insert(0, '../')

import numpy as np
import disk.disk as disk
import event.event as ev

import heapq as pq
import matplotlib.pyplot as plt
from time import sleep



#falta frame

class System:			## ?????????|
    def __init__(self, particles = [], window = None, fpe = None):
    	self.time = 0			#Tiempo de simulación
    	self.minpq = []			# Colisiones del minpq
    	self.particles = particles	#Lista de particulas de system
    	self.turtles = [] 		# Dibujar uno a uno con las particulas
    	self.frame, self.fpe = 0, fpe
    	self.window = window	# Donde ser dibujada


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
        # print("check_colls", t_vert, t_horz)

        if self.time + t_vert <= sim_time:
            event = ev.Event(self.time + t_vert, saucer, None)
            pq.heappush(self.minpq, event)
        if self.time + t_horz <= sim_time:
            event = ev.Event(self.time + t_horz, None, saucer)
            pq.heappush(self.minpq, event)


#----------------------------------------------------------------

    def valid(self, event):
        this_tag, that_tag = event.this_tag, event.that_tag
        this_ocolls, that_ocolls = event.this_colls, event.that_colls
        if this_tag is not None:
            this_ncolls = self.particles[int(this_tag)].num_colls()
            # print("this_ncolls", this_ncolls, "this_ocolls", this_ocolls)
            if this_ncolls > this_ocolls:
                return False				# Compara las del evento con las colisiones actuales
        if that_tag is not None:
            that_ncolls = self.particles[int(that_tag)].num_colls()
            if that_ncolls > that_ocolls:
                return False
        return True

#----------------------------------------------------------------

    def next_valid_event(self):

        while self.minpq != []: #mientras tenga eventos
            event = pq.heappop(self.minpq)
            # print("evento:", event)
            if self.valid(event):
                return event
        return None



#----------------------------------------------------------------
    def move_all_particles(self, event):
        event_time = event.time
        for dish in self.particles:
            dish.move(event_time - self.time)
        self.time = event.time

        # ANIMACION



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

        # print()
        # print("minpq:", len(self.minpq))
        # print()

########################################################################
    # 2.4.1 DEPURACION DE LA IMPLEMENTACION

    def Ptot(self, n): # Terminar de Revisar
        Pt = 0
        for i in range(1, len(self.particles) + 1):
            N = self.particles[i-1]
            Pt += (1/n) * (N.mass * N.speed())
        return Pt
########################################################################


    def main_loop(self, sim_time, fpe=None):
        # listx = []
        # listy = []
        PtotL = []

        fig, ax = plt.subplots()
        fig.set_size_inches(20, 20)
        fig.patch.set_facecolor('xkcd:lightgreen')

        ax.set_facecolor('xkcd:black')
        ax.set_aspect('equal')
        ax.set_xlim(0, 200)
        ax.set_ylim(0, 200)
        ax.set_title('Simulation Collition Particles')
        plt.grid(True, color = 'w')

        for dish in self.particles:
            self.check_colls(dish, sim_time)
            if self.window == True:
                ax.add_artist(dish.obj)
        fig.canvas.draw()

        cont = 0
        while(len(self.minpq) != 0):
            # print()
            # print("minpq", len(self.minpq))
            # print()

            event = self.next_valid_event()
            # print(event)
            if event is None:
                # print("hiIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
                break
            self.move_all_particles(event)
            self.update_velocities(event)
            self.predict_colls(event, sim_time)
            cont += 1
            # print(cont)
            # n = input()

            for k in self.particles:
            # print(k)
            # listx.append(k.x)
            # listy.append(k.y)
                if self.window == True:
                    k.obj.center = k.x, k.y
            fig.canvas.draw()
            plt.pause(0.00000000000001)


        if self.window == True:
            plt.show()
        # print("listx:", listx)
        # print("listy:", listy)

        # return listx, listy
        return PtotL


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
                # idish.obj.center = idish.x, idish.y
