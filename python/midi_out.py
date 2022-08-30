import mido
from main import *

output = mido.open_output('IAC Driver Bus 1')

play = True

output.send(mido.Message('note_on', note=set_note(), velocity=64))
