"""
module to locate shoulder details mannually in cloth 
"""

from pose_estimator import find_rotation_angle
import cv2 as cv
import utils
import numpy as np


def get_shoulder_loc_mannual(cloth_seg):
    "mannually locate shoulder points"

    # crop cloth segmentation
    start_crop, crop_seg = utils.crop_square(cloth_seg)
    crop_seg = cv.cvtColor(crop_seg, cv.COLOR_BGR2GRAY)
    height, width = crop_seg.shape[:2]
    # find right and left shoulder
    #  TODO: take 10% width offset
    offset = int(0.15*width)
    # print(offset)
    