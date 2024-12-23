from PIL import Image
import numpy as np
from PIL import ExifTags

#image_path = 'images/test.png'
def image_to_array(image_path):
    """
    Convert an image to a NumPy array.

    Args:
        image_path (str): The path to the image file.

    Returns:
        np.ndarray: The image represented as a NumPy array.
    """
    #image_path = 'images/test.png'
    image = Image.open(image_path)  # Open the image file

    # Convert the image to raw pixel values
    pixel_data = np.array(image)

    # Calculate number of pixels
    height, width, channels = pixel_data.shape  # Unpack the shape of the array
    total_pixels = height * width  # Calculate total number of pixels

    # Print the total number of pixels
    print(f"Total number of pixels: {total_pixels}")
    return pixel_data

def add_custom_meta_data(image_path, metadata_key, metadata_value):
    """
    Adds custom metadata to an image.

    Args:
        image_path (str): Path to the image file.
        metadata_key (str): Key for the custom metadata.
        metadata_value (str): Value for the custom metadata.
    """
    with Image.open(image_path) as img:
        metadata = img.info
        metadata[metadata_key] = metadata_value
        img.save(image_path)







