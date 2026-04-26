import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

SAMPLERATE = 16000
samples = np.linspace(0, 1, int(SAMPLERATE), endpoint=False)

def make_sine(frequency, amplitude=1.0, duration=1.0):
    samples = np.linspace(0, duration, int(SAMPLERATE * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * samples) * amplitude
    return wave

def make_harmonic(fundamental, n):
    samples = np.linspace(0, 1.0, int(SAMPLERATE * 1.0), endpoint=False)
    wave = np.sin(2 * np.pi * n * fundamental * samples) * 1.0
    return wave

f0 = 220

wave = np.zeros(int(SAMPLERATE * 1.0))
for n in range(1, 6):
    wave = wave + make_harmonic(f0, n)

wave = wave / np.max(np.abs(wave)) 

plt.figure()
plt.plot(samples, wave, label="220 Hz")
plt.xlim(0, 0.02)
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.legend()
plt.title("220 Hz met 4 bovenliggende harmonischen")
plt.show()

sd.play(wave, SAMPLERATE)
sd.wait()