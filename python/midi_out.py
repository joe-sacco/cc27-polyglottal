import mido
# from main import *
#from serial_interface import *

output = mido.open_output('IAC Driver Bus 1')

def send_midi_out(set_note, set_velocity):
    print('🟡🟡🟡🟡🟡🟡🟡🟡🟡 Hello')
    return output.send(mido.Message('note_on', note=set_note, velocity=set_velocity))

