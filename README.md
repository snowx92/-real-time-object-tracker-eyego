#  Real-time object tracker that can follow a specific object in a live webcam feed task by Eyego.
A simple object tracking project with two different tracking implementations:
1. **OpenCV TrackerCSRT** - Fast and lightweight
2. **SiamMask** - Deep learning based with mask segmentation

## Quick Start



### Setup

1. **Clone the repository**
```bash
git clone https://github.com/snowx92/-real-time-object-tracker-eyego.git
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
pip install -r requirements_web.txt
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

## Note about Model Files
Model files are automatically downloaded when you first run the SiamMask tracker. 
The download happens automatically - no manual setup required!

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
├── tracker.py           
├── draw.py              # Draw bounding box
├── selector.py          # Object selection
├── stream.py            # Video stream handling
├── requirements.txt # Python dependencies
├── SiamMask/           # SiamMask implementation
│   ├── tracker.py      # SiamMask tracker
│   └── ...             # SiamMask files
└── README.md           # Instructions
```
