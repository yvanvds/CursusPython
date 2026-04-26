import numpy as np
import matplotlib.pyplot as plt

SAMPLERATE = 16000
frequency = 220
N = 30

samples = np.linspace(0, 1, int(SAMPLERATE), endpoint=False)

def make_sine(frequency, amplitude=1.0, duration=1.0):
    samples = np.linspace(0, duration, int(SAMPLERATE * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * samples) * amplitude
    return wave

def square_wave(fundamental, n_harmonics):
    wave = np.zeros_like(samples)
    for n in range(1, 2 * n_harmonics, 2):
        wave = wave + make_sine(n * fundamental, amplitude=1/n)
    return wave / np.max(np.abs(wave))

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(samples, square_wave(220, N))
plt.xlim(0, 0.02)
plt.ylabel(f"N = {N}")

plt.subplot(2, 1, 2)
plt.plot(samples, np.sign(square_wave(220, N)))
plt.xlim(0, 0.02)
plt.ylabel(f"Real Block")

plt.xlabel("Time (s)")
plt.suptitle("Vergelijking met echte blokgolf")
plt.tight_layout()
plt.show()