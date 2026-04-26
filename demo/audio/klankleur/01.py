import numpy as np
import sounddevice as sd

SAMPLERATE = 16000
duration = 2.0
frequency = 220

samples = np.linspace(0, duration, int(SAMPLERATE * duration), endpoint=False)
wave = np.sin(2 * np.pi * frequency * samples)

sd.play(wave, SAMPLERATE)
sd.wait()