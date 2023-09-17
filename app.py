# type: ignore
'''
Capture a picture every half a second, and output, into a list, when there are green / red lights, as well as the height of the plate.

run using
streamlit run app.py
'''
import cv2
import streamlit as st
import numpy as np
from PIL import Image

cap = cv2.VideoCapture(1)

st.title('Drive Sense  :car:')

def write_bytesio_to_file(filename, bytesio):
    """
    Write the contents of the given BytesIO to a file.
    Creates the file or overwrites the file if it does
    not exist yet. 
    """
    with open(filename, "wb") as outfile:
        # Copy the BytesIO stream to the output file
        outfile.write(bytesio.getbuffer())

def main():
    st.title("Anomaly Detection")
    
    uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "mov"])
    
    # print(type(uploaded_file))
    # print(streamlit.runtime.uploaded_file_manager.UploadedFile.name)

    if uploaded_file is not None:
        # st.video(uploaded_file) 

        # save uploaded video to disc
        temp_file_to_save = 'temporary_vid/temp_file_1.mp4'
        write_bytesio_to_file(temp_file_to_save, uploaded_file)
        
        # # when video is fully saved to disk, open it as BytesIO and play with st.video()
        result_video = open(temp_file_to_save, "rb")

        #show the video on the streamlit app
        st.video(result_video)

        # read it with cv2.VideoCapture(), so now we can process it with OpenCV functions
        cap = cv2.VideoCapture(temp_file_to_save)
        
        frameNr=15
        cur_frame = 0
        success = True

        while success:
            success, frame = cap.read()
            if cur_frame % frameNr == 0:
                print('frame: {}'.format(cur_frame)) 
                pil_img = Image.fromarray(frame)
                # st.image(pil_img)

                #SAVING frame into an image jpg file
                cv2.imwrite(f'temporary_image/current_frame{cur_frame}.jpg', frame )

                

            cur_frame += 1




    return uploaded_file     


#this is to receive the uploaded file.
#assume it's 30 frames per second for a video. Therefore, i'll take a CV capture once every half a second.
def vid(uploaded_file='temporary_vid/temp_file_1.mp4'):
    if file_extension in ["mov", "mp4"]:
        cap = cv2.VideoCapture(uploaded_file)
        frameNr=15
        cur_frame = 0
        success = True

        while success:
            success, frame = vidcap.read()
            if cur_frame % frameNr == 0:
                print('frame: {}'.format(cur_frame)) 
                pil_img = Image.fromarray(frame)
                st.image(pil_img)

                #SAVING frame into an image jpg file
                cv2.imwrite("current_frame", image )

            cur_frame += 1


    return frame



if __name__ == "__main__":
    main()
    # vid()
