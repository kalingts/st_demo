import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Streamlit app title
st.title("Live Webcam Stream with Start Button")

# Button to start the webcam feed
if st.button("Start Camera"):
    # Set up the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        st.error("Error: Unable to access the webcam.")
    else:
        stframe = st.empty()  # Create an empty placeholder for the video frame

        # Display the webcam feed
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

            # Break the loop if the user stops the Streamlit app
            if not st.session_state.get('run', True):
                break

        cap.release()
else:
    st.write("Press the 'Start Camera' button to begin.")
