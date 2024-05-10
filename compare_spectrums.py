from PIL import Image
import numpy as np
from scipy.spatial import distance

def image_to_matrix(image_path):
    # Open the image file
    img = Image.open(image_path)
    # Convert the image data to a numpy array
    img_data = np.asarray(img)
    # Convert the RGB image to grayscale
    img_data_gray = np.dot(img_data[...,:3], [0.2989, 0.5870, 0.1140])
    return img_data_gray

def calculate_correlation(matrix1, matrix2):
    # Flatten the matrices
    matrix1_flat = matrix1.flatten()
    matrix2_flat = matrix2.flatten()
    # Calculate the correlation
    correlation = 1 - distance.correlation(matrix1_flat, matrix2_flat)
    return correlation

def main():
    # Convert the images to matrices
    matrix1 = image_to_matrix('spectrum1.png')
    matrix2 = image_to_matrix('spectrum2.png')
    # Calculate the correlation
    correlation = calculate_correlation(matrix1, matrix2)
    print(f'The correlation between the two images is {correlation}')

if __name__ == "__main__":
    main()