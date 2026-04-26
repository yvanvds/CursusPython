
import numpy as np
import sounddevice as sd

SAMPLERATE = 16000

def my_instrument_1(frequency, duration=1.0, decay=5.0):
    t = np.linspace(0, duration, int(SAMPLERATE * duration), endpoint=False)
    amplitudes = [1.0, 0.3, 0.2, 0.1, 0.05, 0.01]
    
    wave = np.zeros_like(t)
    for n, amp in enumerate(amplitudes, start=1):
        wave = wave + amp * np.sin(2 * np.pi * n * frequency * t)
    
    envelope = np.exp(-decay * t)
    wave = wave * envelope
    return wave / np.max(np.abs(wave))

melody = np.concatenate([
    my_instrument_1(261.63, 0.5),
    my_instrument_1(293.66, 0.5),
    my_instrument_1(329.63, 0.5),
    my_instrument_1(261.63, 0.5),
])
sd.play(melody, SAMPLERATE)
sd.wait()

def my_instrument_2(frequency, duration=1.0, decay=5.0):
    t = np.linspace(0, duration, int(SAMPLERATE * duration), endpoint=False)
    amplitudes = [1.0, 0.8, 0.7, 0.6, 0.07, 0.8]
    
    wave = np.zeros_like(t)
    for n, amp in enumerate(amplitudes, start=1):
        wave = wave + amp * np.sin(2 * np.pi * n * frequency * t)
    
    envelope = np.exp(-decay * t)
    wave = wave * envelope
    return wave / np.max(np.abs(wave))

melody = np.concatenate([
    my_instrument_2(261.63, 0.5),
    my_instrument_2(293.66, 0.5),
    my_instrument_2(329.63, 0.5),
    my_instrument_2(261.63, 0.5),
])
sd.play(melody, SAMPLERATE)
sd.wait()