#  Real-time object tracker that can follow a specific object in a live webcam feed task by Eyego.
A simple object tracking project with two different tracking implementations:
1. **OpenCV TrackerCSRT** - Fast and lightweight
2. **SiamMask** - Deep learning based with mask segmentation

## Quick Start


### Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd object-tracker
```

2. **Create and activate virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Install requirements**
```bash
pip install -r requirements.txt
```

## Running the Trackers

### Option 1: OpenCV Tracker (Recommended for beginners)

Simple and fast tracker using OpenCV's CSRT algorithm.

```bash
python main.py
```

### Option 2: SiamMask Tracker (Advanced)

Deep learning-based tracker with mask segmentation.

1. **Setup SiamMask**
```bash
git clone https://github.com/foolwood/SiamMask
cd SiamMask
pip install -r requirements.txt
```

2. **Run SiamMask tracker**
```bash
cd SiamMask
python tracker.py
```

## Implementation Details

### OpenCV Tracker Architecture

The OpenCV implementation follows a modular design pattern:

**Core Components:**
- **`stream.py`**: Video capture abstraction using `cv2.VideoCapture()`
- **`selector.py`**: ROI selection wrapper for `cv2.selectROI()`
- **`tracker.py`**: Base class with `cv2Tracker` implementing CSRT algorithm
- **`draw.py`**: Visualization utilities for bounding box rendering
- **`main.py`**: Application orchestrator tying all components together

**Technical Implementation:**
```python
# CSRT (Channel and Spatial Reliability Tracker) Algorithm
tracker = cv2.TrackerCSRT_create()
tracker.init(frame, bbox)  # Initialize with first frame
ok, bbox = tracker.update(frame)  # Track in subsequent frames
```


### SiamMask Tracker Architecture

The SiamMask implementation uses a Siamese neural network architecture:

**Core Architecture:**
- **Backbone**: ResNet-50 feature extractor
- **RPN Head**: Region Proposal Network for object localization
- **Mask Head**: Semantic segmentation for pixel-level tracking
- **Template Matching**: Siamese correlation between template and search regions

**Technical Pipeline:**
```python
# Siamese Network Workflow
template = extract_features(template_image)  # 127x127 template
search = extract_features(search_image)      # 255x255 search region
correlation = cross_correlation(template, search)
bbox, mask = rpn_and_mask_heads(correlation)
```




### Code Architecture 

**OpenCV Implementation:**
```python
class cv2Tracker(Base):
    def __init__(self):
        self.tracker = cv2.TrackerCSRT_create()
    
    def init(self, frame, bbox):
        self.tracker.init(frame, bbox)
    
    def update(self, frame):
        return self.tracker.update(frame)
```

**SiamMask Implementation:**
```python
class SiamMaskTester:
    def __init__(self, model_path, device='cpu'):
        self.model = load_pretrained_model(model_path)
        self.template = None
    
    def init(self, frame, bbox):
        self.template = extract_template(frame, bbox)
    
    def track(self, frame, refine=True):
        return siamese_track(frame, self.template, refine)
```


## How to Use

1. Run one of the trackers
2. Select the object you want to track by drawing a bounding box
3. Press ENTER to confirm selection
4. Watch the tracker follow your object
5. Press ESC to quit or R to reset and select a new object

## Tracker Comparison


| Feature                  | OpenCV CSRT                              | SiamMask                              |
|--------------------------|-------------------------------------------|----------------------------------------|
| **Speed**               |  Very Fast                              |  Moderate                            |
| **Accuracy**            |  Good                                   |  Excellent                           |
| **Setup Complexity**    |  Simple                                 |  Complex                             |
| **Dependencies**        |  Light                                  |  Heavy (Requires PyTorch)            |
| **Model Size**          |  ~1MB                                   |  strt with ~45MB                               |
| **Mask Output**         |  No                                     |  Yes                                 |
| **GPU Support**         |  No                                     |  Yes                                 |
| **Real-time Performance** |  Excellent                           |  Good                                |
| **Robustness**          |  Moderate                              |  High                               |
| **Best For**            |  Quick prototyping, real-time apps     |  Research, high accuracy needs       |



## Controls

- **Mouse**: Select object to track
- **ENTER**: Confirm selection
- **ESC**: Quit application  
- **R**: Reset and select new object



### Tips

- Use **OpenCV tracker** for real-time applications
- Use **SiamMask** when you need high accuracy or mask segmentation
- Close other camera applications before running
- Ensure good lighting for better tracking performance

## Requirements

### OpenCV Tracker
- opencv-python
- numpy

### SiamMask Tracker  
- All OpenCV requirements plus:
- PyTorch
- torchvision
- Additional dependencies (see SiamMask/requirements.txt)

## Project Structure

```
object-tracker/
├── main.py              # Main OpenCV tracker app
├── tracker.py           # Alternative OpenCV tracker
├── draw.py              # Visualization utilities
├── selector.py          # Object selection
├── stream.py            # Video stream handling
├── requirements.txt     # Python dependencies
├── SiamMask/           # SiamMask implementation
│   ├── tracker.py      # SiamMask tracker
│   └── ...             # SiamMask files
└── README.md           # This file
```

## License

This project uses code from:
- OpenCV (Apache 2.0 License)
- SiamMask (MIT License)
