import cv2

class video_stream:
    def __init__(self, src=0):
        self.cap = cv2.VideoCapture(src)
    
    def read_frame(self):
        ret , frame = self.cap.read()
        if not ret :
            raise Exception("Camera error")
        return frame
    
    def close_stream(self):
        self.cap.release()
        cv2.destroyAllWindows()      