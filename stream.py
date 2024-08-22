import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

def capture_image():
    # Create a webcam capture object
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Could not open webcam.")
        return None

    # Read a frame from the webcam
    ret, frame = cap.read()
    cap.release()

    if not ret:
        st.error("Could not read frame from webcam.")
        return None

    # Convert frame from BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame_rgb

def main():
    st.title("Webcam Capture and Download")

    if st.button("Capture Image"):
        image = capture_image()
        if image is not None:
            # Display the image
            st.image(image, channels="RGB")

            # Convert image to a PIL image for downloading
            pil_image = Image.fromarray(image)
            buffered = io.BytesIO()
            pil_image.save(buffered, format="PNG")
            img_str = buffered.getvalue()

            # Create a download button
            st.download_button(
                label="Download Image",
                data=img_str,
                file_name="captured_image.png",
                mime="image/png"
            )

if __name__ == "__main__":
    main()
