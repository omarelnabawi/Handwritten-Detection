# OCR with Adaptive Thresholding

This project is a Streamlit-based web app that allows users to upload images and extract text using Optical Character Recognition (OCR) via `EasyOCR`. It provides functionality for preprocessing the uploaded images by applying adaptive thresholding and includes user controls for fine-tuning the thresholding process.

## Features

- **Image Uploading**: Users can upload images (in `.jpg`, `.png`, or `.jpeg` format) for text extraction.
- **Adaptive Thresholding**: The app applies adaptive thresholding on the image to enhance text detection. Users can control two key parameters:
  - **Block Size**: The size of the pixel neighborhood used to calculate the threshold for a pixel.
  - **C Value**: A constant subtracted from the weighted mean to fine-tune the thresholding process.
- **Language Selection**: Supports both English (`en`) and Arabic (`ar`) text detection, allowing the user to choose the language for OCR.
- **Image Transpose**: Option to transpose (rotate) the image before performing text detection.
- **Real-time Image Processing**: As users adjust the thresholding parameters, the processed image is displayed in real-time.
- **OCR with Bounding Boxes**: Once the user clicks the "Start OCR" button, the app detects the text in the image, draws bounding boxes around the detected text, and displays the extracted text below the image.

## Installation

1. Clone the repository:
    ```bash
    git clone <your-repo-url>
    cd <your-repo-folder>
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

1. **Upload an Image**: Use the sidebar to upload an image in `.jpg`, `.png`, or `.jpeg` format.
2. **Control Adaptive Thresholding**:
   - Use the sliders to adjust the `Block Size` and `C Value` to get the best thresholding results for your image.
   - Select whether or not to transpose the image before text detection.
3. **Choose Language**: Select the OCR language (`English` or `Arabic`) from the sidebar.
4. **Start OCR**: Once the image is processed, click the "Start OCR" button in the sidebar to perform text detection.
5. **View Results**: The processed image with bounding boxes around the detected text will be displayed on the main page, along with the extracted text below the image.

## Parameters

- **Block Size**: Controls the size of the neighborhood area used for adaptive thresholding. Must be an odd integer between 3 and 255.
- **C Value**: A constant subtracted from the mean or weighted mean in the adaptive thresholding process. It fine-tunes the thresholding result. Can be any integer between -100 and 100.
- **Transpose Image**: Optionally rotates the image for better orientation during text detection.

## Example

Here is an example of the app’s interface and the text detection result:
![Screenshot](path-to-screenshot)

## Dependencies

- `Streamlit`
- `OpenCV`
- `EasyOCR`
- `Pillow`
- `Numpy`

To install all dependencies, you can use the provided `requirements.txt` file:
```bash
pip install -r requirements.txt
