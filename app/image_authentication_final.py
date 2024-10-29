import image_cryptography
import image_meta_data
import image_to_array
import hash_generator
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

image_path = '../images/test2.jpg'
custom_tag = "XMP:UserComment"

# Load the private key from the PEM file
with open('private_key.pem', 'rb') as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None,  # Add a password if the key is encrypted
        backend=default_backend()
    )

saved_hash_code_encrypted_hex_value = image_meta_data.read_custom_metadata(image_path, custom_tag)
saved_hash_code_encrypted = bytes.fromhex(saved_hash_code_encrypted_hex_value)
print('\nsaved_hash_code_encrypted_hex_value :', saved_hash_code_encrypted_hex_value)
print('\nsaved_hash_code_encrypted :', saved_hash_code_encrypted)
original_hash_code = image_cryptography.decrypt_message(private_key, saved_hash_code_encrypted)

# Call the function for image
pixel_data = image_to_array.image_to_array(image_path)
exif_data = image_cryptography.extract_exif_data(image_path)
hash_code = hash_generator.generate_hash_from_pixel_data(pixel_data)
result2 = image_meta_data.read_all_metadata(image_path)
print("all meta dat :", result2)

if hash_code == original_hash_code:
    print('Image is original')
else:
    print('Image is not original')