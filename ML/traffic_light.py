#traffic light detection
'''

!!! THIS CONTAINS ALL THE INFORMATIONhttps://docs.ultralytics.com/modes/predict/#inference-arguments
'''
import torch
from IPython.display import Image
from ultralytics import YOLO
from PIL import Image, ImageDraw
import numpy as np
import pandas as pd
def traffic_light(image_path = "ML/test_lights.jpg", model_path = "ML/feux_de_circulation.pt", resolution = [800, 600]) -> bool:
    file = model_path
    model = YOLO(model_path)
    # input_image = preprocess_image(image_path)
    # Run the model
    #this is somethow bad# output = model(image_path)

    #each bounding box is the xywh:[the number of arrays in it]
    output2 = model.predict(image_path, imgsz=600, conf=0.10 ,show=True)  #save=True) ==> this saves the image with the box.
    # output3=model.predict(image_path)

    for result in output2:
        boxes = result.boxes  # Boxes object for bbox outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs

    #xyxy values of the box
    # print(boxes.xyxy)
    #return the classes
    # print(list(boxes.cls))

    #return list of floats.
    return [float(x) for x in boxes.cls]




    # answer=output2.pandas().xyxy[0]
    # answer=list(answer.iloc[0])
    # print(output2)# Pandas DataFrame
    # answer=output[0]
    # answer2 = output2
    # print(boxes)
    # print(probs)
    # print(answer2['xywhn'])
    
    # # answer.iloc[0]
    # print(answer.iloc[0])   
    # height = answer['ymax']-answer['ymin']

    # print("height = ", height)
    



print(traffic_light())
# traffic_light()



