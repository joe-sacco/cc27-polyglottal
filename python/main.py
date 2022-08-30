# import serial_interface
import random
from scales import *
# from velocity import *

#scale_calm  # i like this scale very much
#scale_reflective # i like this scale very much
#scale_hopeful
scale = scale_hopeful

def set_note():
    note = random.choice(list(scale.values())) #select random note
    return note

set_note()
# def set_velocity();