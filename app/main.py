import image_to_array
import hash_generator
import image_processing

# Specify the path to your image file
image_path = '../images/test.png'

# Call the function
pixel_data = image_to_array.image_to_array(image_path)

exif_data = image_processing.extract_exif_data(image_path)
# Check if exif_data has any content and print accordingly
if exif_data:  # If EXIF data exists
    print("EXIF Data found:")
    for key, value in exif_data.items():
        print(f"{key}: {value}")
else:  # If no EXIF data found
    print("EXIF data unavailable.")

hash_code = hash_generator.generate_hash_from_pixel_data(pixel_data)
print('Hash code :', hash_code)