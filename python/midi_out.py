import mido

output = mido.open_output('IAC Driver Bus 1')

def send_midi_out(set_note, set_velocity):
    print('🟡🟡🟡 MIDI OUT')
    return output.send(mido.Message('note_on', note=set_note, velocity=set_velocity))

