# Fruit and Vegetable Disease Detector 🍎


## 🌟 Overview

The **Fruit and Vegetable Disease Detector** is an AI-powered application designed to analyze images of fruits and vegetables, classifying them as either healthy or rotten. By leveraging advanced deep learning techniques, it provides highly accurate predictions, making it a valuable tool for quality control in agriculture, food industries, and supply chains. This application automates the inspection process, saving time and effort while reducing human error. Its user-friendly interface, built with **Streamlit**, ensures accessibility for non-technical users. The tool is designed to help minimize food waste, improve efficiency, and support sustainable practices by enabling early identification of quality issues and diseases in produce. Future plans include deploying the application on **Microsoft Azure** for scalability and remote monitoring.


### 📊 Dataset
This project uses the **Fruit and Vegetable Diseases Dataset**, which contains **30,000 images** categorized into healthy and rotten classes for **14 types** of fruits and vegetables.

* **Directories**: Organized into **28 categories** for classification tasks.
* **Sources**: Compiled from Kaggle and GitHub repositories.
* **Image Format**: JPEG/PNG.
* **Image Size**: Recommended resizing to **224x224 pixels** for training consistency.
The dataset is ideal for **image classification** and **deep learning tasks**, enabling **accurate detection of diseases** in fruits and vegetables.


### 🧠 Model
The model is based on **EfficientNetV2B0**, a pre-trained Convolutional Neural Network (CNN) architecture known for its efficiency and accuracy in image classification tasks.

* **Fine-Tuned Layers**: Optimized with additional layers to adapt specifically to this dataset, ensuring accurate detection of diseases in fruits and vegetables.
* **Transfer Learning**: Utilizes pre-trained weights to enhance feature extraction and classification, reducing training time while improving performance.
* **High Accuracy**: Achieves **91.97% accuracy**, making it reliable for real-world applications.
This architecture offers a balance of speed and precision, making it suitable for deployment in quality control systems.

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
- **Deployment Platforms**: Streamlit Cloud and Microsoft Azure(upcoming)

  
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
- **Final Test Accuracy**: **97.42%**
- **Model Type**: EfficientNetV2B0 (Fine-tuned)
- **Dataset Used**: [fruit-and-vegetable-disease-healthy-vs-rotten](https://www.kaggle.com/datasets/muhammad0subhan/fruit-and-vegetable-disease-healthy-vs-rotten/data)

  
---


## 📊 Visualizations

### **Training vs Validation Loss**
![image](https://github.com/user-attachments/assets/08578182-a741-4078-8158-cba187a3110e)



### **Training vs Validation Accuracy**
![image](https://github.com/user-attachments/assets/90656aca-07af-4e6c-bf1a-746527f193a6)


---


## 🎥 Demo Video
[Watch Demo Video](https://drive.google.com/file/d/1eHFBsfeB8dZuW-PqG2YTw_TwXrNkvold/view?usp=sharing)


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
