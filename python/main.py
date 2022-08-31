from serial_interface import *
from scales import *
from midi_out import *
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

def set_velocity():
    return velocity
    
set_note()
send_midi_out(60, 70)
# send_midi_out(set_note(), set_velocity())

def set_wind_strength():
    ser_data = read_serial_data()
    wind_strength = None

    if int(ser_data) >= 0 and int(ser_data) < 10:
        wind_strength = random.randint(0, 10)
    elif int(ser_data) >= 10 and int(ser_data) < 20:
        wind_strength = random.randint(10, 20)
    elif int(ser_data) >= 20 and int(ser_data) < 30:
        wind_strength = random.randint(20, 30)
    elif int(ser_data) >= 30 and int(ser_data) < 40:
        wind_strength = random.randint(30, 40)
    elif int(ser_data) >= 40 and int(ser_data) < 50:
        wind_strength = random.randint(40, 50)
    elif int(ser_data) >= 50 and int(ser_data) < 60:
        wind_strength = random.randint(50, 60)
    elif int(ser_data) >= 60 and int(ser_data) < 70:
        wind_strength = random.randint(60, 70)
    elif int(ser_data) >= 70 and int(ser_data) < 80:
        wind_strength = random.randint(70, 80)
    elif int(ser_data) >= 80 and int(ser_data) < 90:
        wind_strength = random.randint(80, 90)
    elif int(ser_data) >= 90 and int(ser_data) < 127:
        wind_strength = random.randint(90, 100)
    print('🟩🟩🟩🟩🟩', wind_strength)
 
while True: # read serial data on loop
    read_serial_data()
    set_wind_strength()


