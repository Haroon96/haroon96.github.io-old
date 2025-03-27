from PIL import Image
import os
import json
import re
from glob import glob

def build_content_json(photo_dir, old_photos):

    # build dict of existing photos
    existing_photos = { p['photo']: p for p in old_photos }
    
    # create new photos array
    photos = []

    # iterate over all photos
    for photo in sorted(os.listdir(photo_dir), reverse=True):

        # check if already in list or a thumbnail
        if '-thumb' in photo:
            continue

        # get filename
        root, ext = os.path.splitext(photo)
        
        # check if new photo
        if photo not in existing_photos:
            # extract date from name
            date = re.search(r'(?P<y>[0-9]{4})(?P<m>[0-9]{2})(?P<d>[0-9]{2}).*', photo).groupdict()
            # build description
            description = f'{date["m"]}/{date["d"]}/{date["y"]} - '
            # append to photo list
            photos.append({ 'thumbnail': f'{root}-thumb{ext}', 'photo': photo, 'description': description })
        else:
            # append from old list
            photos.append(existing_photos[photo])

    # return new array
    return photos
        

def generate_thumbnails(photo_dir):

    for photo in os.listdir(photo_dir):

        if '-thumb' in photo:
            continue

        root, ext = os.path.splitext(photo)

        photo_path = os.path.join(photo_dir, photo)
        thumb_path = os.path.join(photo_dir, f'{root}-thumb{ext}')

        if os.path.exists(thumb_path):
            continue

        # write thumbnail
        img = Image.open(photo_path)
        
        # crop to square ratio
        if img.width > img.height:
            margin = (img.width - img.height) // 2
            img = img.crop((margin, 0, margin + img.height, img.height))
        else:
            margin = (img.height - img.width) // 2
            img = img.crop((0, margin, img.width, margin + img.width))
        
        img.thumbnail((128, 128))
        img.save(thumb_path)

def main():
    with open('content.json') as f:
        content = json.load(f)

    photo_paths = [
        (os.path.join('src', 'misc', 'photos'), content['misc']['photos']),
        (os.path.join('src', 'photos', 'photos'), content['photos']['photos']),
    ]

    for photo_dir, arr in photo_paths:
        tmp = build_content_json(photo_dir, arr)
        arr.clear()
        arr.extend(tmp)
        generate_thumbnails(photo_dir)

    with open('content.json', 'w') as f:
        json.dump(content, f, indent=4)


def generate_ids():
    json_files = glob('src/data/*.json')
    for json_file in json_files:
        with open(json_file) as f:
            js = json.load(f)
        for idx, entry in enumerate(js):
            entry['id'] = idx
        with open(json_file, 'w') as f:
            json.dump(js, f, indent=2)


if __name__ == '__main__':
    generate_ids()
