from PIL import Image
from PIL.ExifTags import TAGS

def get_time(img_file):
    image = Image.open(img_file)
    return Image.open(img_file)._getexif()[36867] #36867 is for time metadata
