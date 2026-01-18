import sounddevice as sd
import audio_functies as af

toon = af.sine_wave(freq=440, duration=1.0)
#toon = af.gain(toon, factor=0.5)
#toon = af.fade_in(toon, duration=0.1)
#toon = af.fade_in(af.gain(toon, factor=0.5), duration=0.1)

sd.play(toon, af.SAMPLERATE)
sd.wait()