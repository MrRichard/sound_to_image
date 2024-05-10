import matplotlib.pyplot as plt
from create_spectrum import create_spectrum
import librosa

def plot_image(filename='sound.wav', fs=44100):
    # Create the spectrum
    S_dB, sr = create_spectrum(filename, fs)
    
    dpi = 64
    plt.figure(figsize=(256/dpi, 256/dpi), dpi=dpi, frameon=False)
    librosa.display.specshow(S_dB, x_axis=None, y_axis=None, sr=sr, fmax=8000)
    plt.axis('off')

    # Save the plot as a png
    plt.savefig('spectrum.png')

if __name__ == "__main__":
    plot_image()
