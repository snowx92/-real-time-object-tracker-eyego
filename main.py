from stream import video_stream
from tracker import cv2Tracker
from selector import ObjectSelector
from draw import Visualizer
import cv2

class MainApp:
    def __init__(self):
        self.video = video_stream()
        self.tracker = cv2Tracker()

    def run(self):
        frame = self.video.read_frame()
        bbox = ObjectSelector.select(frame)
        self.tracker.init(frame, bbox)

        while True:
            frame = self.video.read_frame()
            ok, bbox = self.tracker.update(frame)
            Visualizer.draw(frame, bbox, ok)
            if cv2.waitKey(1) & 0xFF == 27:
                break

        self.video.close_stream()

if __name__ == "__main__":
    MainApp().run()
