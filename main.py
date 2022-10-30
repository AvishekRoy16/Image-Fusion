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

def get_shoulder_details(self):
    # get shoulder points
    self.shoulder_points = self.get_shoulder_points()
    # step 3: get shoulder width and rotation angle
    # raises: shoulder not found.
    if len(self.shoulder_points) < 2:
        raise Exception("image without shoulder.")

    distance = self.shoulder_points[1][0] - self.shoulder_points[0][0]
    # rotation_angle = find_rotation_angle(self.shoulder_points[0], self.shoulder_points[1])
    return distance
