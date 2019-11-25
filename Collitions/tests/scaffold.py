# disk.py

import numpy as np


LX, LY = 10, 8
VEL_SCALE = .9


class Disk:
    def __init__(self, state=None, mass=1.0, rad=1.0, col=(0, 0, 0), tag=-1)
    def __str__(self)
    def horz_wall_coll(self)
    def vert_wall_coll(self)
    def disk_coll(self, other)
    def move(self, time)
    def update_velocity_vert(self)
    def update_velocity_horz(self)
    def update_velocity_disk(self, other)
    def position(self, pos=None)
    def velocity(self, vel=None)
    def num_colls(self)
    def speed(self)


#############################################################################


# event.py

class Event:
    def __init__(self, t, this, that)
    def __str__(self)
    def __repr__(self)
    def __lt__(self, other)
    def get_time(self)
    def get_tags(self)
    def get_colls(self)


#############################################################################


# frame.py

import turtle as tt
import numpy as np


class Frame:
    def __init__(self, canvheight=None, dims=None, color="black-white")
    def setup_screen(self, sc_dim=None, phy_dim=None)
    def draw_grid(self, stride=None)
    def draw_window(self, strides=None, off=50, lag=None, cm=255)
    def get_scale(self)
    def goto(self, pos)
    def get_pencolor(self)


def setup_artist(saucer, scale)
def rescale(vec, fac, dis)


#############################################################################


# system.py

import numpy as np
import heapq as pq
import turtle as tt
import disk
import event as ev
import frame as fr


class System:
    def __init__(self, particles, window=None, fpe=None)
    def __str__(self)
    def check_colls(self, saucer, sim_time)
    def valid(self, event)
    def next_valid_event(self)
    def move_all_particles(self, event)
    def update_velocities(self, event)
    def predict_colls(self, event, sim_time)
    def main_loop(self, sim_time, fpe=None)
    def write_time_to_screen(self)
    def create_all_artists(self)
    def draw_all_artists(self)
    def set_random_positions(self)


#############################################################################


# __init__.py

"""Motion of two dimensional event-driven physical systems.

Collisions
==========

This package provides...
"""


__all__ = ["disk", "system", "event", "frame"]

PKG_NAME = "collisions"    # package name
PKG_TESTS = "tests"    # test files directory


#############################################################################


# __main__.py

import os
import sys
import __init__


PKG_NAME, TEST_DIR = __init__.PKG_NAME, __init__.PKG_TESTS


def find_py_files(path)
def show_files(tsts)
def assert_correct_dir(cwd, pk_path)
def do_import(tsts, num_test)
def undo_import(tsts, num_test)
def loop_over_menu(tsts_files)


# BEGINNING-OF-EXECUTION
cwd = os.getcwd()
pkg_path = os.path.dirname(os.path.abspath(__file__))
assert_correct_dir(cwd, pkg_path)
tests_path = pkg_path + "/" + TEST_DIR
tests_exist = os.path.isdir(tests_path)

if tests_exist:
    tests_content = os.listdir(tests_path)
    files = find_py_files(tests_content)
    print("\nThere are several test files for this package.")
    loop_over_menu(files)
else:
    print("\nThere are NO test files available for this package.")

print("\ncollisions/{}.py executed".format(__name__))
# END-OF-EXECUTION
