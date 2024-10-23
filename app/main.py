import image_to_array
import hash_generator
import image_cryptography

# Specify the path to your image file
image_path = '../images/test.png'

# Call the function
pixel_data = image_to_array.image_to_array(image_path)

exif_data = image_cryptography.extract_exif_data(image_path)

hash_code = hash_generator.generate_hash_from_pixel_data(pixel_data)
print('Hash code :', hash_code)

# Generate keys
private_key, public_key =image_cryptography.generate_keys()
print('private_key :', private_key, 'public_key :', public_key)

# Message to encrypt
message = hash_code

# Encrypt the message
encrypted = image_cryptography.encrypt_message(public_key, message)
print(f"Encrypted message: {encrypted}")

# Decrypt the message
decrypted = image_cryptography.decrypt_message(private_key, encrypted)
print(f"Decrypted message: {decrypted}")