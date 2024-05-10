import matplotlib.pyplot as plt
from plot_image import plot_image

def save_image(filename='spectrum2.png'):
    # Plot the image
    plot_image()

    # Save the plot as a png
    plt.savefig(filename)

if __name__ == "__main__":
    save_image()
