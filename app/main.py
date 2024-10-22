import image_to_array
import hash_generator

# Specify the path to your image file
image_path = '../images/test.png'
# Call the function
pixel_data = image_to_array.image_to_array(image_path)
hash_code = hash_generator.generate_hash_from_pixel_data(pixel_data)
print('Hash code :', hash_code)