import cv2

class ObjectSelector:
    @staticmethod
    def select(frame):
        return cv2.selectROI("Select Object", frame, False, False)