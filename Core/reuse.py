from PIL import Image
import os

def resize(image,nwidth):
    img = Image.open(image)
    width, height = img.size
    new_width = nwidth
    new_height = int(height * (new_width / width))
    img = img.resize((new_width, new_height))
    # string = random_string(6)
    image_path = os.path.join('images', f'{image.name}')
    img.save(os.path.join('media', image_path), optimize=True, quality=60)

    return image_path