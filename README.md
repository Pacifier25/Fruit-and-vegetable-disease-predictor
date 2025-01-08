# Fruit and Vegetable Disease Detector 🍎

---

## 🌟 Overview
The **Fruit and Vegetable Disease Detector** is an AI-powered application designed to analyze images of fruits and vegetables and classify whether they are healthy or rotten.

This project leverages deep learning techniques to deliver highly accurate predictions, making it a valuable tool for quality control in agriculture and food industries.

---

### 📊 Dataset
This project uses the **Fruit and Vegetable Diseases Dataset**, which contains **30,000 images** categorized into healthy and rotten classes for **14 types** of fruits and vegetables.

* **Directories**: Organized into **28 categories** for classification tasks.
* **Sources**: Compiled from Kaggle and GitHub repositories.
* **Image Format**: JPEG/PNG.
* **Image Size**: Recommended resizing to **224x224 pixels** for training consistency.
The dataset is ideal for **image classification** and **deep learning tasks**, enabling **accurate detection of diseases** in fruits and vegetables.

---

### 🧠 Model
The model is based on **EfficientNetV2B0**, a pre-trained Convolutional Neural Network (CNN) architecture.

* **Fine-Tuned Layers**: Optimized for enhanced performance with this dataset.
* **Transfer Learning** : Leverages pre-trained weights to boost feature extraction and classification accuracy.

---
  

## 🎯 Features
- **Upload Image**: Users can upload images in `.jpg`, `.png`, or `.jpeg` format.  
- **AI-Powered Classification**: Utilizes a **pre-trained deep learning model** to classify images with high accuracy.  
- **Real-Time Feedback**: Displays classification results along with the confidence percentage.  
- **User-Friendly Interface**: Built with **Streamlit** for an intuitive and interactive experience.  

---

## 🛠️ Technology Stack
- **Programming Language**: Python
- **Deep Learning Framework**: TensorFlow/Keras
- **Frontend Framework**: Streamlit
- **Deployment Platforms**: Streamlit Cloud and Microsoft Azure

  
---

  .
## 📂 Folder Structure
```
├── project_files
│   ├── app.py
│   ├── fruit_veg_model.h5
│   ├── fruit_veg_model.keras
├── fruitsand_vegetables.ipynb
└── README.md
```

---


## 📊 Results
- **Final Training Accuracy**: **91.97%**
- **Final Validation Accuracy**: **91.97%**
- **Model Type**: EfficientNetV2B0 (Fine-tuned)
- **Dataset Used**: [fruit-and-vegetable-disease-healthy-vs-rotten](https://www.kaggle.com/datasets/muhammad0subhan/fruit-and-vegetable-disease-healthy-vs-rotten/data)

  
---


## 📊 Visualizations

### **Training vs Validation Loss**


### **Training vs Validation Accuracy**


---


## 🎥 Demo Video
Watch Demo Video


---


## 💻 Installation Guide
### Prerequisites
- **Python** 3.7 or later  
- **Virtual Environment** (optional)

---


### Steps
1. **Clone the Repository**:
```bash
git clone https://github.com/Pacifier25/Fruit_Veg_Detector.git
cd Breast_cancer-
```
2. **Create Virtual Environment**:
```bash
python -m venv env
source env/bin/activate      # For Linux/Mac
env\Scripts\activate         # For Windows
```
3. **Install Dependencies**:
```bash
pip install -r project_files/requirements.txt
```
4. **Run the Application**:
```bash
streamlit run project_files/app.py
```

---

## 🚀 Deployment
The app is currently deployed on Streamlit and will soon be available on Microsoft Azure.

---

## 📥 Download
**[Click here to download the project files](https://github.com/Pacifier25/Fruit-and-vegetable-disease-predictor/archive/refs/heads/main.zip)**


---


## 🙏 Acknowledgements
- **Dataset**: Kaggle - [fruit-and-vegetable-disease-healthy-vs-rotten](https://www.kaggle.com/datasets/muhammad0subhan/fruit-and-vegetable-disease-healthy-vs-rotten/data)  
- **Frameworks**: TensorFlow and Streamlit  
- **Design Elements**:  Agriculture Quality Control Theme
  

---


Thank you for checking out this project! Feel free to contribute or reach out with feedback!
