# 🌙 Low-Light Object Detection in Autonomous Vehicles using YOLOv3 and ExDark Dataset

<p align="center">
  <img src="images/banner.png" width="900">
</p>

## 📌 Overview

Low-light environments such as nighttime roads, tunnels, fog, and poorly illuminated streets significantly reduce the performance of conventional object detection systems used in autonomous vehicles.

This project presents an intelligent **Low-Light Object Detection System** using **YOLOv3** trained with the **COCO** and **ExDark** datasets. The system performs real-time detection of pedestrians, vehicles, traffic signs, and other road objects while providing **voice alerts** to improve driver awareness.

The project focuses on improving detection accuracy under challenging lighting conditions without sacrificing real-time performance.

---

# 🎯 Objectives

- Detect objects accurately in low-light environments.
- Improve autonomous vehicle perception during nighttime.
- Reduce false-negative detections.
- Maintain real-time inference speed.
- Provide audio alerts whenever an object is detected.
- Improve road safety using computer vision and deep learning.

---

# 🚗 Problem Statement

Modern object detection systems perform well under daylight conditions but struggle in:

- Night driving
- Tunnels
- Fog
- Rain
- Poor street lighting

These conditions reduce image quality due to:

- Low brightness
- Noise
- Blur
- Poor contrast

This causes missed detections of important objects such as pedestrians and vehicles, increasing accident risks.

---

# 💡 Proposed Solution

The proposed system combines

- YOLOv3 Object Detection
- ExDark Dataset
- COCO Dataset
- Low-light preprocessing
- Voice Alert System

to create an efficient real-time object detection framework capable of detecting objects even in challenging lighting conditions.

---

# ✨ Features

✅ Real-time object detection

✅ Low-light image detection

✅ Webcam detection

✅ Video file detection

✅ Image detection

✅ Voice alert using Google Text-to-Speech

✅ Bounding boxes with confidence score

✅ GUI built using Tkinter

✅ COCO + ExDark dataset support

✅ Fast YOLOv3 inference

---

# 🏗 System Architecture

```
             Input Image / Video
                      │
                      ▼
        Image Preprocessing
 (Brightness Enhancement, Noise Reduction)

                      │
                      ▼
          YOLOv3 Object Detector

                      │
        ┌─────────────┴──────────────┐
        ▼                            ▼

 Bounding Boxes             Detected Labels

        ▼                            ▼
    Display Output           Voice Alert (gTTS)

```

---

# 📂 Project Structure

```
ObjectDetection/

│

├── comparison/

├── datasets/

├── model/

│ ├── yolov3.cfg

│ ├── yolov3.weights

│ ├── yolov3-labels

│

├── play/

├── Main.py

├── ObjectDetection.py

├── comp.py

├── cam_test.py

├── compmatrix.py

├── ft.py

├── ssmatrix.py

├── requirements.txt

├── coco.names

├── run.bat

└── README.md

```

---

# ⚙️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| OpenCV | Image Processing |
| YOLOv3 | Object Detection |
| NumPy | Numerical Computing |
| Tkinter | GUI |
| Google Text-to-Speech | Voice Alert |
| Playsound | Audio Playback |

---

# 📚 Datasets

## COCO Dataset

- Large-scale object detection dataset
- General object categories
- Used for base object recognition

---

## ExDark Dataset

Specialized dataset containing images captured in:

- Night
- Dim light
- Indoor darkness
- Street lighting
- Low illumination

Used to improve low-light detection accuracy.

---

# 🧠 Model

YOLOv3

Backbone:

Darknet-53

Advantages

- Fast
- Accurate
- Real-time
- Lightweight
- Suitable for autonomous vehicles

---

# 🔄 Workflow

```
Start

↓

Load YOLOv3 Model

↓

Load Labels

↓

Select Image / Video / Webcam

↓

Image Preprocessing

↓

YOLOv3 Detection

↓

Draw Bounding Boxes

↓

Display Result

↓

Generate Voice Alert

↓

End

```

---

# 🖥 GUI

The application provides a simple Tkinter interface with buttons to:

- Load YOLO Model
- Detect using Webcam
- Detect from Image
- Detect from Video
- Exit Application

---

# 🔊 Voice Alert System

Whenever an object is detected, the system announces:

```
Detected Objects:

Car

Person

Traffic Light

Bicycle

```

using Google Text-to-Speech (gTTS).

---

# 📈 Performance

| Metric | Value |
|---------|--------|
| Model | YOLOv3 |
| Dataset | COCO + ExDark |
| mAP | **0.68** |
| Processing | Real-time |
| FPS | Approximately **20–25 FPS** (depending on hardware) |

---

# 💻 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Low-Light-Object-Detection.git
```

---

## Go to Project

```bash
cd Low-Light-Object-Detection
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python Main.py
```

---

# 📦 Requirements

- Python 3.x
- OpenCV
- NumPy
- TensorFlow
- Keras
- gTTS
- Playsound

---

# 📷 Sample Results

## Normal Light

(Add Screenshot)

---

## Low-Light Detection

(Add Screenshot)

---

## Webcam Detection

(Add Screenshot)

---

## Voice Alert

(Add Screenshot)

---

# 📊 Advantages

- High detection accuracy
- Real-time performance
- Works under poor lighting
- User-friendly GUI
- Audio notification
- Easy deployment
- Suitable for intelligent transportation

---

# 🚧 Limitations

- Uses only camera input
- Performance decreases in complete darkness
- Requires YOLOv3 weights
- Limited by available GPU/CPU resources

---

# 🔮 Future Scope

- Upgrade to YOLOv8
- Transformer-based object detection
- Edge AI deployment (Jetson Nano, Raspberry Pi)
- Sensor fusion with LiDAR and Radar
- Multi-camera support
- Driver fatigue monitoring
- Traffic sign recognition
- Lane detection
- Cloud deployment
- Mobile application

---

# 📖 Research Publication

This project has been prepared as an IEEE conference paper titled:

**Enhancing Low-Light Object Detection in Autonomous Vehicles Using YOLOv3 and ExDark Dataset**

---

# 👨‍💻 Authors

**Pallerla Sohan**

B.E Information Technology

Hyderabad, Telangana, India

GitHub:

https://github.com/sohanpallerla

LinkedIn:

https://linkedin.com/in/pallerla-sohan-ba79a8246

---

# 🙏 Acknowledgements

- Vasavi College of Engineering
- Department of Information Technology
- COCO Dataset
- ExDark Dataset
- OpenCV
- YOLOv3

---

# ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.

---

# 📜 License

This project is developed for educational and research purposes.

MIT License.
