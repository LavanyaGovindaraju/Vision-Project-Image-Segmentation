
# Vision-Project-Image-Segmentation

This repository contains the implementation of image segmentation tasks using three different models across three distinct tasks. The models were evaluated on various datasets, achieving significant performance metrics.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Tasks and Results](#tasks-and-results)
- [Contributing](#contributing)

## Introduction
In this project, we implemented image segmentation using three different models for three separate tasks. Each task involves a different model and dataset to showcase the versatility and effectiveness of our segmentation approaches.

## Installation
To run the project, ensure you have Python installed. Follow the steps below to set up your environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/LavanyaGovindaraju/Vision-Project-Image-Segmentation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Vision-Project-Image-Segmentation
   ```

## Usage
To run the image segmentation tasks, you can use the provided Python scripts and Jupyter notebooks. Here are examples of how to execute the main scripts:

1. Run Task 1:
   ```bash
   python Vision_task2_main.py
   ```
2. Run Task 2:
   ```bash
   python Vision_task3_main.py
   ```

## Project Structure
The repository is structured as follows:

```
Vision-Project-Image-Segmentation/
│
├── Vision_task_1.ipynb           # Jupyter Notebook for Task 1
├── Vision_task_1_final.ipynb     # Final version of Task 1 Notebook
├── Vision_task2_main.py          # Main script for Task 2
├── Vision_task3_main.py          # Main script for Task 3
├── network2.py                   # Network definition for Task 2
├── network3.py                   # Network definition for Task 3
├── evalutaion.py                 # Evaluation script
├── Output2.py                    # Output script for Task 2
├── Output3.py                    # Output script for Task 3
├── Report.pdf                    # Project report
└── README.md                     # Project README
```

## Tasks and Results

### Task 1
- **Description**: Implemented the VGG-16 pretrained model on the PascalVoc 2012 Dataset.
- **Dataset**: PascalVoc 2012
- **Metrics**:
  - F1-score: 0.8560
  - Dice-coefficient: 0.7482

### Task 2
- **Description**: Implemented the R2-UNet model as described in [this paper](https://arxiv.org/ftp/arxiv/papers/1802/1802.06955.pdf) on the CityScape dataset.
- **Dataset**: CityScape
- **Training Metrics**:
  - Accuracy: 0.9904
  - Sensitivity: 0.8713
  - Specificity: 0.9950
  - F1-score: 0.8713
  - Jaccard score: 0.7720
- **Testing Metrics**:
  - Accuracy: 0.9843
  - Sensitivity: 0.8042
  - Specificity: 0.9918
  - F1-score: 0.8042
  - Jaccard score: 0.6725

### Task 3
- **Description**: Improved the results of Task 2 by combining the R2-UNet model with an attention gate.
- **Dataset**: CityScape
- **Training Metrics**:
  - Accuracy: 0.9982
  - Sensitivity: 0.8854
  - Specificity: 0.9932
  - F1-score: 0.88632
  - Jaccard score: 0.8056
- **Testing Metrics**:
  - Accuracy: 0.9862
  - Sensitivity: 0.8323
  - Specificity: 0.9543
  - F1-score: 0.8413
  - Jaccard score: 0.7523

## Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push your branch and create a pull request.

