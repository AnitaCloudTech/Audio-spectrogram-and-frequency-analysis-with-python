import numpy as np
import wave
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.signal import spectrogram

def load_audio(file_path):
    with wave.open(file_path, 'rb') as wav_file:
        n_channels = wav_file.getnchannels()
        sampwidth = wav_file.getsampwidth()
        framerate = wav_file.getframerate()
        n_frames = wav_file.getnframes()

        frames = wav_file.readframes(n_frames)
        signal = np.frombuffer(frames, dtype=np.int16)
        if n_channels > 1:
            signal = signal[::n_channels]

    return signal, framerate

def plot_waveform(signal, sr, title="Waveform"):
    time = np.linspace(0, len(signal) / sr, num=len(signal))
    plt.figure(figsize=(10, 4))
    plt.plot(time, signal)
    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.show()

def plot_spectrogram(signal, sr, title="Spectrogram"):
    f, t, Sxx = spectrogram(signal, sr)
    plt.figure(figsize=(10, 4))
    plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud', cmap='magma')
    plt.colorbar(label="Intensity (dB)")
    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.show()

def calculate_energy(signal):
    energy = np.sum(signal ** 2) / len(signal)
    return energy

def calculate_fundamental_frequency(signal, sr):
    n = len(signal)
    freq_spectrum = np.fft.fft(signal)
    freqs = np.fft.fftfreq(n, d=1/sr)

    magnitude = np.abs(freq_spectrum[:n // 2])
    freqs = freqs[:n // 2]

    fundamental_freq_index = np.argmax(magnitude)
    fundamental_frequency = freqs[fundamental_freq_index]

    return fundamental_frequency

file_paths = ["Aa.wav", "I.wav", "O.wav", "N.wav", "T.wav"]  

for file_path in file_paths:
    try:
        signal, sr = load_audio(file_path)

        plot_waveform(signal, sr, title=f"Waveform: {file_path}")
        plot_spectrogram(signal, sr, title=f"Spectrogram: {file_path}")

        energy = calculate_energy(signal)
        print(f"Energy of {file_path}: {energy}")

        fundamental_frequency = calculate_fundamental_frequency(signal, sr)
        print(f"Fundamental frequency of {file_path}: {fundamental_frequency} Hz")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
