import image_to_array
import hash_generator
import image_cryptography
from PIL import Image

# Specify the path to your image file
image_path = '../images/test2.jpg'
#image_path = '../images/test.png'
#image_path = '../images/test3.jpg'

# Call the function
pixel_data = image_to_array.image_to_array(image_path)
#exif_data = image_cryptography.extract_exif_data(image_path)

hash_code = hash_generator.generate_hash_from_pixel_data(pixel_data)
print('Hash code :', hash_code)

# Generate keys
private_key, public_key = image_cryptography.generate_keys()
print('private_key and public_key have been generated')

# Message to encrypt
message = hash_code

# Encrypt the message
encrypted = image_cryptography.encrypt_message(public_key, message)
print(f"Encrypted message: {encrypted}")
# Save the hash to a file
with open("hash_code_encrypted.txt", "w") as file:
    file.write(encrypted.hex())
print(f"Hash code saved as encrypted hex value:", encrypted.hex())

#image_to_array.add_custom_meta_data(image_path, 'custom_meta_data', encrypted.hex())
img = Image.open(image_path)
# Extract existing EXIF data
exif_data = img.getexif()
print('exif data :', exif_data)
# Modify existing metadata
exif_data[0x9286] = encrypted.hex()  # 0x9286 is the tag for 'UserComment'
# Save the image with new EXIF metadata
img.save('../images/new_modified_test2.jpg', exif=exif_data)
img = Image.open('../images/new_modified_test2.jpg')
# Extract existing EXIF data
exif_data = img.getexif()
print('new exif data :', exif_data)
