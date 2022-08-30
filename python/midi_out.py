import mido
from main import *

output = mido.open_output('IAC Driver Bus 1')
output.send(mido.Message('note_on', note=set_note(), velocity=set_velocity()))
