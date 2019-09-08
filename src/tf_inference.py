import os
import argparse
import io
import glob
import hashlib
from pathlib import Path
from PIL import Image
import subprocess

import tensorflow as tf
from object_detection.utils import dataset_util


def create_tf_example(img_path:str,
                      annotation_path:str,
                     class_names:dict):
    
    # ------------------------------------------------------------
    # Read the image
    with tf.gfile.GFile(img_path, 'rb') as fid:
        encoded_img = fid.read()

    encoded_img_io = io.BytesIO(encoded_img)
    image = Image.open(encoded_img_io)
    img_width, img_height = image.size
    print(image.size)
    
    key = hashlib.sha256(encoded_img).hexdigest()
    
    fn = Path(img_path).stem
    
    # ------------------------------------------------------------
    # Read the annotation
    
    x_1,y_1,x_2,y_2 = [],[],[],[]
    clss_list = []
    with open(annotation_path, 'r') as li:
        annotations = li.readlines()
        for i in annotations:
            print(i.strip().split(' '))
            label,float(x),float(y),float(w),float(h) = i.strip().split(' ')
            x_1.append(float(x - (w / 2)))
            y_1.append(float(y - (h / 2)))
            x_2.append(float(x + (w / 2)))
            y_2.append(float(y + (h / 2)))
            clss_list.append(int(label))
    
    # --------------------------------------------------------------
    # (user): Populate the following variables from your example.
    width = 0
    height = 100 # Image width , Image height
    filename = fn # Filename of the image. Empty if image is not from file
    encoded_image_data = encoded_img # Encoded image bytes
    image_format = b'jpeg' # b'jpeg' or b'png'

    xmins = x_1 # List of normalized left x coordinates in bounding box (1 per box)
    ymins = y_1 # List of normalized top y coordinates in bounding box (1 per box)
    xmaxs = x_2 # List of normalized right x coordinates in bounding box (1 per box)
    ymaxs = y_2 # List of normalized bottom y coordinates in bounding box (1 per box)

    classes_text = [k for class_names.values()] # List of string class name of bounding box (1 per box)
    classes = clss_list # List of integer class id of bounding box (1 per box)

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_image_data),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
      }))
    
    return tf_example


if __name__ == "__main__":
    DATASET_PATH = "/home/nj/HBRS/RnD/Dataset/DoorDetect-Dataset/dataset"
    TF_FILE_PATH = "/home/nj/HBRS/RnD/Dataset/DoorDetect-Dataset/tf_data_new.tfrecord"

    class_names = {0:"door",
              1:"handle",
              2:"cabinet door",
              3:"refrigerator door"}

    writer =  tf.io.TFRecordWriter(TF_FILE_PATH)

    img_file_list = glob.glob(os.path.join(DATASET_PATH,"*.jpg"), recursive=True)

    for i,img in enumerate(img_file_list) :
        name = Path(img).stem

        img_path = os.path.join(DATASET_PATH , name + ".jpg")
        annotation_path = os.path.join(DATASET_PATH ,name  + ".txt")
    
        print(img_path)
    
        tf_record = create_tf_example(img_path,annotation_path,class_names)
        writer.write(tf_record.SerializeToString())
    
    #     print(i," ",name," written to tf record.")
        break