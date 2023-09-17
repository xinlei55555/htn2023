# type: ignore
import cv2
import streamlit as st
import numpy as np

cap = cv2.VideoCapture(1)

st.title('Drive Sense  :car:')
def main():
    st.title("Anomaly Detection")
    
    uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "mov"])
    
    if uploaded_file is not None:
        st.video(uploaded_file)      


def vid(uploaded_file):
    if file_extension in ["mov", "mp4"]:
      cap = cv2.VideoCapture(uploaded_file)
      cur_frame = 0
      success = True

      while success:
        success, frame = vidcap.read()
        if cur_frame % frame_skip == 0:
            print('frame: {}'.format(cur_frame)) 
            pil_img = Image.fromarray(frame)
            st.image(pil_img)
        cur_frame += 1
    return frame

if __name__ == "__main__":
    main()
