# -- coding: utf-8 --

import datetime
import json
import os
import re
import fnmatch
from PIL import Image
import numpy as np
from pycococreatortools import pycococreatortools
 
ROOT_DIR = "/home/comp/qiangwang/mmdetection/data/car" #
IMAGE_DIR = "/home/comp/qiangwang/mmdetection/data/car/test" # 
JSON_DIR = "/home/comp/qiangwang/mmdetection/annotations" 
ANNOTATION_DIR = os.path.join(ROOT_DIR, "annotations") # 
 
INFO = {
    "description": "Example Dataset",
    "url": "https://github.com/waspinator/pycococreator",
    "version": "0.1.0",
    "year": 2018,
    "contributor": "waspinator",
    "date_created": datetime.datetime.utcnow().isoformat(' ')
}
 
LICENSES = [
    {
        "id": 1,
        "name": "Attribution-NonCommercial-ShareAlike License",
        "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/"
    }
]
 
CATEGORIES = [
        {
            "supercategory": "none",
            "id": 0,
            "name": "ignored regions"
        },
        {
            "supercategory": "none",
            "id": 1,
            "name": "pedestrian"
        },
        {
            "supercategory": "none",
            "id": 2,
            "name": "people"
        },
        {
            "supercategory": "none",
            "id": 3,
            "name": "bicycle"
        },
        {
            "supercategory": "none",
            "id": 4,
            "name": "car"
        },
        {
            "supercategory": "none",
            "id": 5,
            "name": "van"
        },
        {
            "supercategory": "none",
            "id": 6,
            "name": "truck"
        },
        {
            "supercategory": "none",
            "id": 7,
            "name": "tricycle"
        },
        {
            "supercategory": "none",
            "id": 8,
            "name": "awning-tricycle"
        },
        {
            "supercategory": "none",
            "id": 9,
            "name": "bus"
        },
        {
            "supercategory": "none",
            "id": 10,
            "name": "motor"
        },
        {
            "supercategory": "none",
            "id": 11,
            "name": "others"
        }
]



def filter_for_jpeg(root, files):
    file_types = ['*.jpeg', '*.jpg', '*.png']
    file_types = r'|'.join([fnmatch.translate(x) for x in file_types])
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if re.match(file_types, f)]
    
    return files
 
def filter_for_annotations(root, files, image_filename):
    file_types = ['*.png']
    file_types = r'|'.join([fnmatch.translate(x) for x in file_types])
    basename_no_extension = os.path.splitext(os.path.basename(image_filename))[0]
    file_name_prefix = basename_no_extension + '.*'
    files = [os.path.join(root, f) for f in files]
    files = [f for f in files if re.match(file_types, f)]
    files = [f for f in files if re.match(file_name_prefix, os.path.splitext(os.path.basename(f))[0])]
 
    return files
 
def main():
 
    coco_output = {
        "images": [],
        "categories": CATEGORIES,
    }
 
    image_id = 1
    
    # filter for jpeg images
    for root, _, files in os.walk(IMAGE_DIR):
        image_files = filter_for_jpeg(root, files)
 
        # go through each image
        for image_filename in image_files:
            image = Image.open(image_filename)
            image_info = pycococreatortools.create_image_info(
                image_id, os.path.basename(image_filename), image.size)
            coco_output["images"].append(image_info)
            image_id = image_id + 1
 
    with open('{}/car_4k.json'.format(JSON_DIR), 'w') as output_json_file:
        json.dump(coco_output, output_json_file)
 
 
if __name__ == "__main__":
    main()
