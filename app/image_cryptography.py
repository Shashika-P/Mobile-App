from PIL import Image
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def extract_exif_data(image_path):
    # Open an image file
    with Image.open(image_path) as image:
        # Extract EXIF data
        exif_data = image.getexif()

    # Check if exif_data has any content and print accordingly
    if exif_data:  # If EXIF data exists
        print("EXIF Data found:")
        for key, value in exif_data.items():
            print(f"{key}: {value}")
    else:  # If no EXIF data found
        print("EXIF data unavailable.")

def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()

    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()  # If no passphrase is used
    )
    # Save the key to a file PEM format
    with open('private_key.pem', 'wb') as f:
        f.write(pem)

    pem_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    # Save the key to a file PEM format
    with open('public_key.pem', 'wb') as f:
        f.write(pem_public)

    return private_key, public_key


def encrypt_message(public_key, message: str):
    encrypted_message = public_key.encrypt(
        message.encode('utf-8'),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_message

def decrypt_message(private_key, encrypted_message):
    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted_message.decode('utf-8')