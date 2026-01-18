import audio_functies as af
import sounddevice as sd
import numpy as np

notes = []
notes.append(af.midi_to_freq(48))
notes.append(af.midi_to_freq(43))
notes.append(af.midi_to_freq(45))
notes.append(af.midi_to_freq(40))
notes.append(af.midi_to_freq(41))
notes.append(af.midi_to_freq(36))
notes.append(af.midi_to_freq(38))
notes.append(af.midi_to_freq(31))
notes.append(af.midi_to_freq(36))

waves = []
for note in notes:
    wave = af.instrument(note, duration=2)
    waves.append(wave)

melody = af.melody(waves)
melody = af.fade_out(melody, duration=1.0)

sd.play(melody, af.SAMPLERATE)
sd.wait()


