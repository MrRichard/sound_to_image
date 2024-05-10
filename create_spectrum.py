import numpy as np
import librosa
import soundfile as sf

def create_spectrum(filename='sound.wav', sr=44100):
    
    y, sr = librosa.load(filename)
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)

    # Convert to log scale (dB)
    S_dB = librosa.power_to_db(S, ref=np.max)

    # Return the spectrogram
    return S_dB, sr

if __name__ == "__main__":
    create_spectrum()