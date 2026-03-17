# Lunar Crater Detection (YOLOv8)

A small computer vision project (prototype) to detect lunar craters using orbital imagery from Chandrayaan-2 OHRC.

## Overview
This project builds a prototype pipeline for crater detection:
- preprocess orbital strip images
- tile into smaller patches
- label craters
- train a YOLOv8 object detection model
- reconstruct detections on original strips

## Data
Source: Chandrayaan-2 Orbiter High Resolution Camera (OHRC)  
(Downloaded from ISSDC; not included due to size)

## Method
- Preprocessing: grayscale + normalization + histogram equalization  
- Tiling: 256×256 tiles with metadata for reconstruction  
- Filtering: removed low-texture tiles  
- Annotation: bounding boxes around crater rims (YOLO format)  
- Model: YOLOv8n, 50 epochs, image size 256  

## Requirements
- numpy
- opencv-python
- ultralytics (YOLOv8)
- pandas
- matplotlib

## Results
- Precision: 0.81048
- Recall: 0.64444
- F1 score: 0.72000