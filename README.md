# AI Data Classification Using K-Nearest Neighbors (KNN)

## Overview

This project demonstrates the implementation of a supervised machine learning classification model using the K-Nearest Neighbors (KNN) algorithm. The system classifies Iris flower species based on sepal and petal measurements by applying data preprocessing, feature scaling, model training, prediction, and performance evaluation techniques.

The project was developed as part of the DecodeLabs Artificial Intelligence Internship Program to understand the fundamentals of supervised learning and classification algorithms.

---

## Features

* Iris dataset classification
* Data preprocessing and preparation
* Feature scaling using StandardScaler
* Train-test data splitting
* K-Nearest Neighbors (KNN) classification
* Performance evaluation using:

  * Accuracy Score
  * F1 Score
  * Classification Report
  * Confusion Matrix
* Visualization of classification results

---

## Project Structure

```text
AI-Data-Classification/
│
├── outputs/
│   ├── confusion_matrix.png
│   └── results.txt
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── visualize.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-Learn

---

## Dataset

The project uses the Iris dataset available in the Scikit-Learn library.

### Dataset Information

* Total Samples: 150
* Features: 4
* Classes: 3

### Features

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

### Target Classes

* Iris Setosa
* Iris Versicolor
* Iris Virginica

---

## Workflow

```text
Dataset Loading
       ↓
Data Preprocessing
       ↓
Feature Scaling
       ↓
Train-Test Split
       ↓
KNN Model Training
       ↓
Prediction
       ↓
Performance Evaluation
       ↓
Confusion Matrix Visualization
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/Bommana-suchitra/Task-2-Bommana-Suchitra-Decodelabs.git
```

### Navigate to Project Directory

```bash
cd Task-2-Bommana-Suchitra-Decodelabs
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

```bash
python main.py
```

---

## Evaluation Metrics

The model is evaluated using:

* Accuracy Score
* F1 Score
* Classification Report
* Confusion Matrix

---

## Results

The trained KNN model successfully classifies Iris flower species with high prediction accuracy and generates detailed evaluation metrics along with a confusion matrix visualization.

---

## Future Enhancements

* Hyperparameter tuning
* Comparison with other classification algorithms
* Random Forest implementation
* Logistic Regression implementation
* Model deployment using Flask or FastAPI
* Web-based prediction interface

---

## Learning Outcomes

Through this project, the following machine learning concepts were implemented and understood:

* Supervised Learning
* Data Preprocessing
* Feature Scaling
* Classification Algorithms
* Model Evaluation
* Data Visualization

---

## Author

**Bommana Suchitra**

Artificial Intelligence Internship Program
DecodeLabs
