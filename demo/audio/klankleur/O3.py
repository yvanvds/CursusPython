import numpy as np
import sounddevice as sd

SAMPLERATE = 16000

def make_sine(frequency, amplitude=1.0, duration=1.0):
    samples = np.linspace(0, duration, int(SAMPLERATE * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * samples) * amplitude
    return wave

f0 = 220

wave = make_sine(f0)
# wave = wave + make_sine(2 * f0) 
# wave = wave + make_sine(3 * f0)
# wave = wave / np.max(np.abs(wave)) 

sd.play(wave, SAMPLERATE)
sd.wait()