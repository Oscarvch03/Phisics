# system.py

import sys
sys.path.insert(0, '../')

import numpy as np
import disk.disk as disk
import event.event as ev

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

        if self.time + t_vert <= sim_time:
            event = ev.Event(self.time + t_vert, saucer, None)
            pq.heappush(self.minpq, event)
        if self.time + t_horz <= sim_time:
            event = ev.Event(self.time + t_horz, None, saucer)
            pq.heappush(self.minpq, event)


#----------------------------------------------------------------

    def valid(self, event):
    	this_tag, that_tag = event.get_tags()
    	this_ocolls, that_ocolls = event.get_colls()

    	if this_tag is not None:
    		this_ncolls = self.particles[this_tag].num_colls()
    		if this_ncolls > this_ocolls:
    			return False				# Compara las del evento con las colisiones actuales

    	if that_tag is not None:
    		that_ncolls = self.particles[that_tag].num_colls()
    		if that_ncolls > that_ocolls:
    			return False

    	return True

#----------------------------------------------------------------

    def next_valid_event(self):
    	self.frame += 1
    	while self.minpq != []: #mientras tenga eventos
    		event = pq.heappop(self.minpq)
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
            self.particles[tag_a].update_velocity_disk(self.particles[tag_b])
        elif tag_a is not None and tag_b is None:
            self.particles[tag_a].update_velocity_vert()
        elif tag_a is None and tag_b is not None:
            self.particles[tag_b].update_velocity_horz()


    def predict_colls(self, event, sim_time):
        tag_a, tag_b = event.this_tag, event.that_tag

        if tag_a is not None:
            self.check_colls(self.particles[tag_a], sim_time)

        if tag_b is not None:
            self.check_colls(self.particles[tag_b], sim_time)




    def main_loop(self, sim_time, fpe=None):
        for dish in self.particles:
            self.check_colls(dish, sim_time)

        # ANIMACION

        while(len(self.minpq) != 0):
            event = self.next_valid_event()
            if event is None:
                break
            self.move_all_particles(event)
            self.update_velocities(event)
            self.predict_colls(event, sim_time)

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
                idish.obj.center = idish.x, idish.y
