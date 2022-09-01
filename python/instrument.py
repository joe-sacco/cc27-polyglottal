from serial_interface import *
from scales import *
from midi_out import *
# from main import *

import random
import json
from time import sleep
# from velocity import *

########### INSTRUMENT ############


# #MAIN
# @app.get("/railway")
# def read_railway_data():
#     return api.read_railway_data()
# #APPY
# def read_railway_data():
#     with open('data/railway.json', 'r', encoding='utf-8', errors='ignore') as stream:
#         data = json.load(stream)

#MAIN
#APPY
# def read_scale_data():
#     with open('data/scale.json', 'r', encoding='utf-8', errors='ignore') as stream:
#         data = json.load(stream)
#     return data

    
#scale_calm  # i like this scale very much
#scale_reflective # i like this scale very much
#scale_hopeful

scale = scale_hopeful #send_scale(scale_setting)
velocity = 60

# while True:
#     sleep(2)
#     print('🟡🟡🟡🟡🟡🟡🟡🟡', scale)

def set_wind_strength():
    ser_data = read_serial_data()
    print('🟩🟩🟩 SERIAL', ser_data)
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
    elif int(ser_data) >= 90 and int(ser_data) < 120:
        wind_strength = random.randint(90, 100)
    return int(wind_strength)

def set_note():
    note = random.choice(list(scale.values())) #select random note
    print('🟠🟠🟠', note)
    return note

def set_velocity():
    velocity = int(set_wind_strength())
    print('🟥🟥🟥 VELOCITY', velocity)
    return velocity

def play_notes():
    while(True):
        if read_serial_data() != 0:
            set_wind_strength()
            delay = abs(set_wind_strength() - 100) / 50
            print('🟦🟦🟦 DELAY', delay)
            #note_frequency = set_wind_strength()
            time.sleep(delay)
            send_midi_out(set_note(), set_velocity())
            # read_serial_data() # read serial data on loop
        else:
            sleep(1)

# def print_serial():
#     while(True): # read serial data on loop
#         read_serial_data()
#         set_wind_strength()


play_notes()

# print_serial()







# if int(ser_data) >= 0 and int(ser_data) < 10:
#         wind_strength = random.randint(0, 10)
#     elif int(ser_data) >= 10 and int(ser_data) < 20:
#         wind_strength = random.randint(10, 20)
#     elif int(ser_data) >= 20 and int(ser_data) < 30:
#         wind_strength = random.randint(20, 30)
#     elif int(ser_data) >= 30 and int(ser_data) < 40:
#         wind_strength = random.randint(30, 40)
#     elif int(ser_data) >= 40 and int(ser_data) < 50:
#         wind_strength = random.randint(40, 50)
#     elif int(ser_data) >= 50 and int(ser_data) < 60:
#         wind_strength = random.randint(50, 60)
#     elif int(ser_data) >= 60 and int(ser_data) < 70:
#         wind_strength = random.randint(60, 70)
#     elif int(ser_data) >= 70 and int(ser_data) < 80:
#         wind_strength = random.randint(70, 80)
#     elif int(ser_data) >= 80 and int(ser_data) < 90:
#         wind_strength = random.randint(80, 90)
#     elif int(ser_data) >= 90 and int(ser_data) < 127:
#         wind_strength = random.randint(90, 100)