import cv2

class Base:
    def init(self, frame, bbox):
        raise NotImplementedError

    def update(self, frame):
        raise NotImplementedError

class cv2Tracker(Base):
    def __init__(self):
        self.tracker = cv2.TrackerCSRT_create() 

    def init(self, frame, bbox):
        self.tracker.init(frame, bbox)

    def update(self, frame):
        ok, bbox = self.tracker.update(frame)
        return ok, bbox
