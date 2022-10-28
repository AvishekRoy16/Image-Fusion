import cv2 as cv
import imutils
import logging


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
