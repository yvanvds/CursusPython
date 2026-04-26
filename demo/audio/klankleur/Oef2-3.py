import numpy as np
import sounddevice as sd

SAMPLERATE = 16000

def make_sine(frequency, amplitude=1.0, duration=1.0):
    samples = np.linspace(0, duration, int(SAMPLERATE * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * samples) * amplitude
    return wave

wave = make_sine(880, amplitude=0.4, duration=0.5)

sd.play(wave, SAMPLERATE)
sd.wait()