from pose_estimator import PoseEstimator
import custom_shoulder_locator
from segmentation import cloth_extractor
import utils

import cv2 as cv
import imutils
import logging

#TODO: create error list
ERROR_LIST = [] # e.g. shoulder detection error
MIN_SHOULDER_DISTANCE=0

class CMate:
    def __init__(self, source_img, dest_img):
        self.source_img = source_img
        self.dest_img = dest_img
        self.dest_pose_estimator = PoseEstimator(cv.imread(self.dest_img))
        self.source_pose_estimator = None  # initialize after cloth extraction
        self.error_list = []

def find_rotation_angle(a, b):
    """
    find angle a of right angled traingle with ab as hypotenous
    <)bac
    """
    try:
        c = (b[0], a[1])
        ratio = (c[1]-b[1])/(c[0]-a[0])
        # print("ratio",ratio)
        angle = math.degrees(math.atan(ratio))
        return angle
    except ZeroDivisionError:
        raise Exception("left shoulder and right shoulder detected at same location.")
