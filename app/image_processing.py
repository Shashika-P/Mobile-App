from PIL import Image
from PIL import ExifTags
def extract_exif_data(image_path):
    # Open an image file
    with Image.open(image_path) as image:
        # Extract EXIF data
        exif_data = image.getexif()

        # Print EXIF data
        for tag_id, value in exif_data.items():
            tag = Image.ExifTags.TAGS.get(tag_id, tag_id)
            print(f"{tag}: {value}")
