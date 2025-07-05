# Audio-spectrogram-and-frequency-analysis-with-python
This mini project implements audio signal analysis techniques in python, focusing on processing vowel and consonant sounds recorded from speech samples.
The main functionalities include:

- Loading `.wav` audio files
- Plotting waveform (time-domain signal)
- Plotting spectrogram (frequency content over time)
- Calculating signal energy
- Estimating the fundamental frequency of the audio signal

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- SciPy

You can install the required packages using:

```bash
pip install numpy matplotlib scipy
```
Usage
1.Prepare your audio .wav files (e.g., recordings of vowels and consonants) and place them in the project directory.

2.Update the file_paths list in the script to include the filenames you want to analyze.

3.Run the script:
```bash
python domaci.py
```
The script will display waveform and spectrogram plots for each audio file, and print energy and fundamental frequency values in the console.
Files
domaci.py — main Python script for loading audio files and performing analysis.

Example audio files: Aa.wav, I.wav, O.wav, N.wav, T.wav
Explanation
Waveform shows the amplitude of the signal over time.

Spectrogram shows how the frequency content of the signal changes over time.

Energy is a measure of the signal’s power.

Fundamental frequency is the lowest frequency of a periodic waveform, often related to the perceived pitch.
