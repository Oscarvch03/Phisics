# event.py

class Event:
    def __init__(self, t, this, that):
        self.time = t
        self.this_tag = None if this is None else this.tag
        self.that_tag = None if this is None else that.tag
        self.this_colls = None if this is None else this.num_colls
        self.that_colls = None if that is None else that.num_colls

    def __str__(self):
        str = "Begin Event: \n"
        str += " Time: {:.2f} \n".format(self.time)
        str += " Particle: {} {} \n".format(self.this_tag, self.this_colls)
        str += " Particle: {} {} \n".format(self.that_tag, self.that_colls)
        str += "End Event. \n"
        return str

    def __repr__(self):
        str = "{:.2f}".format(self.time)
        str += "{} {}".format(self.this_tag, self.that_tag)
        str += "{} {}".format(self.this_colls, self.that_colls)
        return str

    def __lt__(self, other):
        return self.time < other.time
