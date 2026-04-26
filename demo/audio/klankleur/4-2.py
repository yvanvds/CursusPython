import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

SAMPLERATE = 16000
samples = np.linspace(0, 1, int(SAMPLERATE), endpoint=False)

f0 = 220
N = 40

def make_sine(frequency, amplitude=1.0, duration=1.0):
    samples = np.linspace(0, duration, int(SAMPLERATE * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * samples) * amplitude
    return wave

wave = np.zeros_like(samples)
for n in range(1, N + 1, 2):
    wave = wave + make_sine(n * f0, amplitude=1/n)

wave = wave / np.max(np.abs(wave))

plt.figure(figsize=(10, 3))
plt.plot(samples, wave)
plt.xlim(0, 0.02)
plt.xlabel("Time (s)")
plt.title("Blokgolf (enkel oneven harmonischen)")
plt.show()

sd.play(wave, SAMPLERATE)
sd.wait()