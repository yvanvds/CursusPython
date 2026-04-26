
import numpy as np
import sounddevice as sd

SAMPLERATE = 16000

def my_instrument(frequency, duration=1.0, decay=5.0):
    t = np.linspace(0, duration, int(SAMPLERATE * duration), endpoint=False)
    amplitudes = [1.0, 0.3, 0.2, 0.1, 0.05, 0.01]
    
    wave = np.zeros_like(t)
    for n, amp in enumerate(amplitudes, start=1):
        wave = wave + amp * np.sin(2 * np.pi * n * frequency * t)
    
    envelope = np.exp(-decay * t)
    wave = wave * envelope
    return wave / np.max(np.abs(wave))

freq = 220
melody = np.array([])
for n in range(1, 14):
    melody = np.concatenate([melody, my_instrument(freq, duration=0.5)])
    freq = freq * 2**(1/12)


sd.play(melody, SAMPLERATE)
sd.wait()