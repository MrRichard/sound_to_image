import sounddevice as sd
import numpy as np
import soundfile as sf

def record_sound(filename='sound.wav', duration=3, fs=44100):
    print('Recording...')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    print('Recording finished')
    sf.write(filename, myrecording, fs)  # Save as WAV file 
    return filename

if __name__ == "__main__":
    record_sound()
