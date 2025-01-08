import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Set page configuration with title and favicon
st.set_page_config(
    page_title="🍎 Fruit & Veggie Detector",
    page_icon="🍎",  # Emoji icon as favicon
)

# Set Background Image and CSS
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1606787366850-de6330128bfc");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.5);
}

/* File Uploader Box Styling */
.stFileUploader > div {
    border: 2px dashed #000000 !important; /* Black Border */
    background-color: rgba(255, 255, 255, 0.8) !important; /* Light Background */
    padding: 20px !important;
    border-radius: 10px !important;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1) !important; /* Subtle shadow */
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Title
st.markdown("<h2 style='text-align: center; font-family: Arial, sans-serif; font-weight: bold; color: black;'>🍎 Fruit & Vegetable Disease Detector</h2>", unsafe_allow_html=True)

# Load the model
model = load_model('fruit_veg_model.h5')

# Define class names
class_names = [
    "Apple__Healthy", "Apple__Rotten", "Banana__Healthy", "Banana__Rotten",
    "Bellpepper__Healthy", "Bellpepper__Rotten", "Carrot__Healthy", "Carrot__Rotten",
    "Cucumber__Healthy", "Cucumber__Rotten", "Grape__Healthy", "Grape__Rotten",
    "Guava__Healthy", "Guava__Rotten", "Jujube__Healthy", "Jujube__Rotten",
    "Lemon__Healthy", "Lemon__Rotten", "Mango__Healthy", "Mango__Rotten",
    "Orange__Healthy", "Orange__Rotten", "Pomegranate__Healthy", "Pomegranate__Rotten",
    "Potato__Healthy", "Potato__Rotten", "Tomato__Healthy", "Tomato__Rotten"
]

# Preprocessing Function
def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Prediction Function
def predict_image(image):
    predictions = model.predict(image)
    predicted_class = class_names[np.argmax(predictions)]
    confidence = np.max(predictions)
    return predicted_class, confidence

# File Uploader Box
st.markdown("<h2 style='text-align: center; font-family: Arial, sans-serif; font-weight: bold; color: black;'>🍎 Upload an Image</h2>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="📷 Uploaded Image", use_container_width=True)
    st.write("Processing...")

    # Preprocess and Predict
    processed_image = preprocess_image(image)
    label, confidence = predict_image(processed_image)

    # Display Prediction Results
    st.markdown(f"<h2 style='font-family: Arial, sans-serif; font-weight: bold; color: grey;'>📊 Prediction: <span style='color: white;'>{label}</span></h2>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-family: Arial, sans-serif; color: lightgreen;'>🔄 Confidence: <span style='color: white;'>{confidence * 100:.2f}%</span></h3>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 22px; font-family: Arial, sans-serif; font-weight: bold; color: black;'>📧 Contact Us: piyushbist10@gmail.com</p>",
    unsafe_allow_html=True
)
