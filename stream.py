import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Live Webcam Stream")

# Set up the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    st.error("Error: Unable to access the webcam.")
else:
    stframe = st.empty()  # Create an empty placeholder for the video frame

    while True:
        ret, frame = cap.read()  # Capture frame-by-frame

        if not ret:
            st.error("Error: Unable to read from the webcam.")
            break

        # Convert the frame to RGB format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert to PIL image
        img = Image.fromarray(frame_rgb)

        # Display the image in Streamlit
        stframe.image(img, use_column_width=True)

cap.release()
