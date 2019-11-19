import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import random

class InteractiveCircle:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, 200)
        self.ax.set_ylim(0, 200)

        self.circ = Circle((10, 10), 3)
        self.ax.add_artist(self.circ)
        self.ax.set_title('Clic to move the circle')

        self.fig.canvas.mpl_connect('button_press_event', self.on_click)

    def on_click(self, event):
        if event.inaxes is None:
            return
        temp = [(random.randint(3, 197), random.randint(3, 197)) for j in range(50)]
        for i in temp:
            print(i)
            self.circ.center = i[0], i[1]
            self.fig.canvas.draw()
            plt.pause(1)

    def show(self):
        plt.show()


InteractiveCircle().show()
