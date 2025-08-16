# 📓 YOLOv8 Training & Real-Time Inference

---

## 1. Introduction

* Short explanation of YOLOv8 and its use cases.
* Workflow overview: **dataset → training → evaluation → visualization → real-time inference**.

---

## 2. Setup

* Install and import required libraries (Roboflow, Ultralytics, OpenCV, Matplotlib).
* Environment check.

---

## 3. Dataset Preparation

* Download dataset from **Roboflow** (Rock-Paper-Scissors).
* Split into `train`, `val`, and `test`.
* Generate `data.yaml` file with paths and class names.

---

## 4. Training YOLOv8

* Initialize model (e.g., `yolov8n.pt`).
* Train on dataset (epochs, batch size, image size).
* Store outputs in structured folders.

---

## 5. Training Results Visualization

* Display `results.png` (training curves).
![](run-yolov8-training/exp1/results.png)
* Display `confusion_matrix.png` (class-wise evaluation).
* ![](run-yolov8-training/exp1/confusion_matrix.png)
* Interpret metrics briefly.

---

## 6. Model Evaluation

* Load trained weights (`best.pt`).
* Run inference on test set.
* Save results into prediction folder.

---

## 7. **Images Section (Visualization of Predictions)**

This section focuses only on **visual results**:

![](runs/detect/predict/egohands-public-1620849871605_png_jpg.rf.566b1b47cbd3b1558121ca2e797f5ff7.jpg)
![](runs/detect/predict/Photo-on-2-16-22-at-10-20-AM-16_jpg.rf.77e43b8cc06d204239d719afc63ae511.jpg)
![](runs/detect/predict/IMG_7077_MOV-82_jpg.rf.ecaa5de681a7d56dcbea4a17f49caac8.jpg)
![](runs/detect/predict/IMG_5567_mp4-16_jpg.rf.d32a3cb377e3bc260a0a841e47831a4a.jpg)

---

## 8. Real-Time Camera Inference

* Open webcam feed.
* Run model on live frames.
* Draw bounding boxes, labels, confidence scores.
* Show FPS counter.
* Exit with “q” key.

