#traffic light detection

import torch
from IPython.display import Image
from ultralytics import YOLO
# import os 
# import random
# import shutil
 
# from sklearn.model_selection import train_test_split
from PIL import Image, ImageDraw
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

def traffic_light(image_path = "ML/test_lights_2.jpg", model_path = "ML/feux_de_circulation.pt", resolution = [800, 600]) -> bool:
    file = model_path
    # model = your (396, 660) (396, 660) (396, 660) (396, 660) (396, 660)_model()
    #don't forget to install pip ultralytics!
    model = YOLO(model_path)
    # model = torch.hub.load('ultralytics/yolov8s', 'custom', path=model_path) 
    # the preprocessing is NOT useful.
    # input_image = preprocess_image(image_path)
    # Run the model
    output = model(image_path)
    output2 = model.predict(image_path, save=True, imgsz=600, conf=0.10)
    output3=model.predict(image_path)

    for result in output:
        boxes = result.boxes  # Boxes object for bbox outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs

    # answer=output.pandas().xyxy[0]
    # answer=list(answer.iloc[0])
    print(output)# Pandas DataFrame
    answer=output[0]
    answer2 = output2
    print(boxes)
    print(probs)
    return answer2
    # # answer.iloc[0]
    # print(answer.iloc[0])   
    # height = answer['ymax']-answer['ymin']

    # print("height = ", height)



traffic_light()




