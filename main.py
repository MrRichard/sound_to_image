import record_sound
import create_spectrum
import plot_image
import save_image

def main():
    # Record the sound
    sound_file = record_sound.record_sound()

    # Create the spectrum
    create_spectrum.create_spectrum(sound_file)

    # Plot the image
    plot_image.plot_image(sound_file)

    # Save the image
    save_image.save_image()

if __name__ == "__main__":
    main()
