from serial_interface import *
from scales import *
import random
# from velocity import *

#scale_calm  # i like this scale very much
#scale_reflective # i like this scale very much
#scale_hopeful
scale = scale_hopeful
velocity = 60

def set_note():
    #note = random.choice(list(scale.values())) #select random note
    note = read_serial_data()
    return note

set_note()

def set_velocity():
    return velocity

while True: # read serial data on loop
    read_serial_data()
