import os
from glob import glob
from itertools import chain
from PIL import Image

def generate_thumbnails():
    extensions = ['jpeg', 'jpg', 'png']
    photos = chain(*[glob(f'public/images/**/*.{ext}') for ext in extensions])
    for photo in photos:

        if 'thumbnail' in photo:
            continue

        # extract photo path and name
        photo_dir = os.path.dirname(photo)
        basename = os.path.basename(photo)
        thumb_path = os.path.join(photo_dir, f'thumbnail_{basename}')

        # skip if thumbnail already exists
        if os.path.exists(thumb_path):
            continue

        # write thumbnail
        img = Image.open(photo)
        
        # crop to square ratio
        if img.width > img.height:
            margin = (img.width - img.height) // 2
            img = img.crop((margin, 0, margin + img.height, img.height))
        else:
            margin = (img.height - img.width) // 2
            img = img.crop((0, margin, img.width, margin + img.width))
        
        # save thumbnail
        img.thumbnail((128, 128))
        img.save(thumb_path)

if __name__ == '__main__':
    generate_thumbnails()