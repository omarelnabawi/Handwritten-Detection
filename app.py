import cv2
import easyocr
import numpy as np
import streamlit as st
from PIL import Image

# Function to process the image using adaptive thresholding
def process_image(img, block_size, c_value, transpose):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Optional transposing if selected
    if transpose:
        img = cv2.transpose(img)
        img = cv2.flip(img, 0)
    
    # Apply adaptive threshold with user-controlled parameters
    adaptive_threshold = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, c_value
    )
    return adaptive_threshold, img

# Function to extract text from the image
def extract_text(img, language):
    reader = easyocr.Reader([language])
    result = reader.readtext(img)
    return result

# Streamlit App
st.title("OCR with Adaptive Thresholding")

# Sidebar controls
st.sidebar.header("Thresholding Parameters")
block_size = st.sidebar.slider("Block Size", 3, 255, step=2, value=255)
c_value = st.sidebar.slider("C Value", -100, 100, step=1, value=40)

# Language selection
language = st.sidebar.selectbox("Choose Language", ["en", "ar"])

# Transpose option
transpose_img = st.sidebar.checkbox("Transpose Image", value=False)

# Image uploader
uploaded_file = st.sidebar.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = np.array(Image.open(uploaded_file))

    # Display the uploaded image
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Apply the thresholding and display the result
    processed_img, transposed_img = process_image(img, block_size, c_value, transpose_img)
    st.image(processed_img, caption="Processed Image with Adaptive Threshold", use_column_width=True, clamp=True)

    # Perform OCR when button is clicked
    if st.sidebar.button("Start OCR"):
        result = extract_text(processed_img, language)

        # Draw bounding boxes and extracted text on the image
        img_with_boxes = transposed_img.copy() if transpose_img else img.copy()
        words = []
        for detection in result:
            top_left = tuple([int(val) for val in detection[0][0]])
            bottom_right = tuple([int(val) for val in detection[0][2]])
            text = detection[1]
            words.append(text)
            font = cv2.FONT_HERSHEY_SIMPLEX
            img_with_boxes = cv2.rectangle(img_with_boxes, top_left, bottom_right, (255, 0, 0), 2)
            img_with_boxes = cv2.putText(img_with_boxes, text, top_left, font, 1, (255, 0, 0), 2, cv2.LINE_AA)

        # Display image with bounding boxes
        st.image(img_with_boxes, caption="Image with Detected Text", use_column_width=True)

        # Show the extracted text
        extracted_text = ' '.join(words)
        st.subheader("Extracted Text")
        st.write(extracted_text)
