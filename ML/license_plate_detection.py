'''
#here is my source: https://blog.paperspace.com/train-yolov5-custom-data/

Run the File inside the yolov5 folder


#getting the data
#dataset: https://public.roboflow.com/object-detection/license-plates-us-eu/3
#https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data

Yolo V5 repository
# !git clone https://github.com/ultralytics/yolov5  # clone repo
# !pip install -U -r yolov5/requirements.txt  # install dependencies
# %cd /content/yolov5

#command to run to run the yolo algorithm
python detect.py --weights runs/train/yolo_road_det/weights/best.pt --img 416 --conf 0.4 --source ../test_infer.jpg


running the yolo algorithm in a file
https://github.com/ultralytics/yolov5/issues/36
'''

import torch
from IPython.display import Image
# import os 
# import random
# import shutil
# from sklearn.model_selection import train_test_split
from PIL import Image, ImageDraw
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

file = "ML/best_model.pt"
# model = your_model()
#don't forget to install pip ultralytics!
model = torch.hub.load('ultralytics/yolov5', 'custom', path=file)  # local model


#  model.load_state_dict(torch.load(file))


# Function to preprocess the image before feeding it to the model
# def preprocess_image(image_path):
    # img = Image.open(image_path).convert("RGB")
    # img = img.resize((224, 224))  # Resize to the model's expected input size
    # img = np.array(img).astype(np.float32) / 255.0  # Convert to a NumPy array and normalize
    # img = np.transpose(img, (2, 0, 1))  # Transpose the image to (channels, height, width)
    # img = np.expand_dims(img, axis=0)  # Add a batch dimension
    # return torch.tensor(img)


# Load the image and preprocess it
image_path = "ML/test_infer.jpg"
# the preprocessing is NOT useful.
# input_image = preprocess_image(image_path)

# Run the model
output = model(image_path)

print(output)

print(output.pandas().xyxy[0])  # Pandas DataFrame

# print('torch %s %s' % (torch.__version__, torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CPU'))

# random.seed(0)

# class_id_to_name_mapping = dict(zip(class_name_to_id_mapping.values(), class_name_to_id_mapping.keys()))

# def plot_bounding_box(image, annotation_list):
#     annotations = np.array(annotation_list)
#     w, h = image.size
    
#     plotted_image = ImageDraw.Draw(image)

#     transformed_annotations = np.copy(annotations)
#     transformed_annotations[:,[1,3]] = annotations[:,[1,3]] * w
#     transformed_annotations[:,[2,4]] = annotations[:,[2,4]] * h 
    
#     transformed_annotations[:,1] = transformed_annotations[:,1] - (transformed_annotations[:,3] / 2)
#     transformed_annotations[:,2] = transformed_annotations[:,2] - (transformed_annotations[:,4] / 2)
#     transformed_annotations[:,3] = transformed_annotations[:,1] + transformed_annotations[:,3]
#     transformed_annotations[:,4] = transformed_annotations[:,2] + transformed_annotations[:,4]
    
#     for ann in transformed_annotations:
#         obj_cls, x0, y0, x1, y1 = ann
#         plotted_image.rectangle(((x0,y0), (x1,y1)))
        
#         plotted_image.text((x0, y0 - 10), class_id_to_name_mapping[(int(obj_cls))])
    
#     plt.imshow(np.array(image))
#     plt.show()

# annotations = "/mnt/DATA/Personnel/Other learning/Programming/Personal_projects/3_Hackathons_with_buddies/HackTheNorth2023/data/valid/images/d5f4069e6734ac06_jpg.rf.a56a7fe6fa63495583c618e5deccee88.jpg"

# # Get any random annotation file 
# annotation_file = random.choice(annotations)
# with open(annotation_file, "r") as file:
#     annotation_list = file.read().split("\n")[:-1]
#     annotation_list = [x.split(" ") for x in annotation_list]
#     annotation_list = [[float(y) for y in x ] for x in annotation_list]

# #Get the corresponding image file
# image_file = annotation_file.replace("annotations", "images").replace("txt", "png")
# assert os.path.exists(image_file)

# #Load the image
# image = Image.open(image_file)

# #Plot the Bounding Box
# plot_bounding_box(image, annotation_list)  
