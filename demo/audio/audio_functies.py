import matplotlib.pyplot as plt
import numpy as np

SAMPLERATE = 16000

def sine_wave(freq, duration, amplitude=0.5):
    """
    Genereer een sinusgolf.

    freq       : frequentie in Hz
    duration   : duur in seconden
    amplitude  : volume (0.0 – 1.0)
    """
    t = np.linspace(
        0,
        duration,
        int(SAMPLERATE * duration),
        endpoint=False
    )

    y = amplitude * np.sin(2 * np.pi * freq * t)
    return y

def gain(y, factor):
    """
    Pas het volume aan van een waveform.

    y      : array met samples
    factor : vermenigvuldigingsfactor
    """
    return y * factor

def silence(duration):
    """
    Genereer stilte.

    duration : duur in seconden
    """
    n_samples = int(SAMPLERATE * duration)
    return np.zeros(n_samples)

def mix(wave1, wave2):
    """
    mix twee waveforms door ze op te tellen. Ze moeten even lang zijn.

    wave1 : array met samples
    wave2 : array met samples
    """
    return wave1 + wave2

def fade_in(y, duration):
    """
    Pas een fade-in toe op een waveform.

    y        : array met samples
    duration : duur van de fade-in in seconden
    """
    n_fade = int(SAMPLERATE * duration)
    fade_curve = np.linspace(0.0, 1.0, n_fade)

    y[:n_fade] *= fade_curve
    return y

def fade_out(y, duration):
    """
    Pas een fade-out toe op een waveform.

    y        : array met samples
    duration : duur van de fade-out in seconden
    """
    n_fade = int(SAMPLERATE * duration)
    fade_curve = np.linspace(1.0, 0.0, n_fade)

    y[-n_fade:] *= fade_curve
    return y

def plucked(y, attack_duration=0.01, decay_duration=0.3):
    """
    Simuleer het geluid van een geplukte snaar.

    y                : array met samples
    attack_duration  : duur van de attack in seconden
    decay_duration   : duur van de decay in seconden
    """
    n = len(y)

    attack = int(SAMPLERATE * attack_duration)
    decay  = int(SAMPLERATE * decay_duration)

    attack = max(1, min(attack, n))
    decay  = max(1, min(decay, n - attack))

    sustain_level = 0.3

    e = np.ones(n) * sustain_level

    # attack: 0 → 1
    u = np.linspace(0.0, 1.0, attack, endpoint=False)
    e[:attack] = 0.5 - 0.5 * np.cos(np.pi * u)

    # decay: 1 → sustain_level
    e[attack:attack+decay] = np.linspace(1.0, sustain_level, decay, endpoint=False)
    y_new = y * e
    return y_new

def lfo(y, freq, depth):
    """
    Pas een Low Frequency Oscillator (LFO) toe op een waveform.

    y     : array met samples
    freq  : frequentie van de LFO in Hz
    depth : diepte van de LFO (0.0 – 1.0)
    """
    n = len(y)
    t = np.linspace(0, n / SAMPLERATE, n, endpoint=False)

    lfo_wave = (1.0 + depth * np.sin(2 * np.pi * freq * t)) / (1.0 + depth)
    y_new = y * lfo_wave
    return y_new

def white_noise(duration, amplitude=0.5):
    """
    Genereer witte ruis.

    duration  : duur in seconden
    amplitude : volume (0.0 – 1.0)
    """
    n_samples = int(SAMPLERATE * duration)
    y = amplitude * np.random.uniform(low=-1.0, high=1.0, size=n_samples)
    return y


def plot_wave_segment(y, t0=0.0, t1=0.02, title="Waveform"):
    """
    Toon een kort deel van een waveform.

    y  : array met samples
    t0 : starttijd (s)
    t1 : eindtijd (s)
    """
    i0 = int(t0 * SAMPLERATE)
    i1 = int(t1 * SAMPLERATE)

    segment = y[i0:i1]
    t = np.linspace(t0, t1, len(segment), endpoint=False)

    plt.figure(figsize=(8, 3))
    plt.plot(t, segment)
    plt.xlabel("tijd (s)")
    plt.ylabel("amplitude")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_wave_segments(waves, titles, t0=0.0, t1=0.02):
    n = len(waves)
    plt.figure(figsize=(8, 3 * n))

    for i, (y, title) in enumerate(zip(waves, titles)):
        i0 = int(t0 * SAMPLERATE)
        i1 = int(t1 * SAMPLERATE)

        segment = y[i0:i1]
        t = np.linspace(t0, t1, len(segment), endpoint=False)

        plt.plot(t, segment)
        
    plt.xlabel("tijd (s)")
    plt.ylabel("amplitude")
    plt.title(title)
    plt.grid(True)
    plt.show()

def melody(waves):
    return np.concatenate(waves)

def instrument(freq, duration):
    n = int(SAMPLERATE * duration)
    t = np.linspace(0, duration, n, endpoint=False)

    y = np.zeros(n)
    for i, a in enumerate([1.0, 0.5, 0.25, 0.125]):
        y += sine_wave(freq * (i + 1), duration, amplitude=a)
        
    y = lfo(y, freq=3, depth=0.5)

    y += lfo(white_noise(duration, amplitude=0.02), 6, depth=0.7)

    

    y = plucked(y, attack_duration=0.005, decay_duration=0.2)
    return y

def midi_to_freq(m):
    """
    Zet een MIDI-nootnummer om naar een frequentie in Hz.
    m = 69 komt overeen met A4 = 440 Hz.
    """
    return 440.0 * (2.0 ** ((m - 69) / 12))