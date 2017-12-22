'''
  Information:
  * Date: 2017-12-21
  * Brief: add thug_life tag for image
  * Author: haskellcg

  Platform: 
  * Windows7_x64
  * Python3.6_x64
      
  Libs:
  * dlib (pip install dlib-19.8.1-cp36-cp36m-win_amd64.whl)
    * numpy
  * moviepy (pip install moviepy)
    * decorator
    * imageio
    * olefile
    * pillow
    * tqdm
  * imutils (pip install imutils)
  * cv2 (pip install opencv-python)
    
  Problems:
  * NeedDownloadError('Need ffmpeg exe. 'imageio.core.fetching.NeedDownloadError: 
    Need ffmpeg exe. You can download it by calling: 
    imageio.plugins.ffmpeg.download() => 按照报错操作即可
  
'''

import dlib
import argparse
import numpy as np
import moviepy.editor as mpy

from PIL import Image
from imutils import face_utils

src_image_file_path = "./resources/thug_life_creation_1.jpg"

parser = argparse.ArgumentParser()
parser.add_argument("-image", required = False, help = "path to input image")
args = parser.parse_args()

test_image_file_path = args.image
if test_image_file_path == None:
    test_image_file_path = src_image_file_path

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(test_image_file_path)

