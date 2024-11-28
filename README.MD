# Varroa Detector
![Roboflow Trained Badge](https://img.shields.io/badge/Trained%20with-Roboflow-orange.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A computer vision tool that detects Varroa destructor mites on honey bees using deep learning. This project aims to help beekeepers monitor the health of their colonies by automatically detecting these harmful parasites.

## Model Performance

- **mAP (Mean Average Precision)**: 91.7%
- **Precision**: 82.7%
- **Recall**: 84.9%

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Dataset & Training](#dataset--training)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [License](#license)

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/nolan667/varroa-detector.git
cd varroa-detector
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install roboflow pillow tk
```

## Usage

1. Run the application:
```bash
python varroa_detector.py
```

2. Using the interface:
   - Select an image from the list on the left
   - Preview will appear in the center
   - Click "Analyze" to process the image
   - Results will show the number of detected Varroa mites
   - A new window will open with the annotated image

## Dataset & Training

### Dataset Creation
- The dataset was manually created and annotated
- Images were collected from various honey bee colonies in france
- Contains high-resolution photographs of beehive floor with visible Varroa mites
- Images were taken under different lighting conditions and angles

### Annotation Process
1. Manual annotation using Roboflow's annotation tool
2. Each Varroa mite was carefully marked with bounding boxes

### Training Details
- Model trained using Roboflow's platform
- YOLOv8 architecture
- Training parameters:
  - Confidence threshold: 20%
  - Overlap threshold: 25%
- Data augmentation techniques used:
  - Rotation
  - Brightness adjustment
  - Contrast variation

## Project Structure

```
varroa-detector/
│
├── varroa_detector.py      # Main application file
├── dataset/               # Directory containing test images
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## Technical Details

### Features
- Real-time Varroa mite detection
- User-friendly GUI interface
- Batch processing capabilities
- Detection confidence scores
- Annotated output images

### Dependencies
- Roboflow: API integration and model hosting
- Pillow: Image processing
- Tkinter: GUI framework
- Custom YOLOv8 model

### Performance Optimization
- Efficient image preprocessing
- Optimized inference settings
- Memory-efficient image handling

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

⭐ If this project helped you, please consider giving it a star on GitHub!