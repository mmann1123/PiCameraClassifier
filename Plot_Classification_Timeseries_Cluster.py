restart_df = True

# run from python
import scripts.label_image 
from scripts.read_tensor_from_image_file import read_tensor_from_image_file
from scripts.load_labels import load_labels
from scripts.load_graph import load_graph
import sys
import numpy as np
import tensorflow as tf
import os
from datetime import datetime
import matplotlib.pyplot as plt
import os
from PIL import Image, ImageDraw, ImageFont
import time
import psutil
import pandas as pd


input_height = 224
input_width = 224
input_mean = 128
input_std = 128
input_layer = "input"
output_layer = "final_result"
ARCHITECTURE = "mobilenet_1.0_224"
label_file = r'/home/mmann1123/Documents/PiCameraClassifier/tf_files/'+ARCHITECTURE+'_retrained_labels.txt'
model_file = r'/home/mmann1123/Documents/PiCameraClassifier/tf_files/'+ARCHITECTURE+'_retrained_graph.pb'
 

###############################
# iterate across series of photos 
os.chdir(r'/home/mmann1123/Dropbox/Apps/PiCameraLogger/')
rootdir = os.getcwd()

# set up storage for classifications or load existing csv of classifications
if restart_df == True: 
    df = pd.DataFrame(columns=['Path','Date','Class','Prob'])
else:
    df = pd.read_csv('/home/mmann1123/Documents/PiCameraClassifier/predicted_labels.csv', index_col=0)

for dir, dirs, files in os.walk(rootdir):
    for file in files:
        if file == '.dropbox' or file =='predicted_labels.csv'or len(df[df['Path'].str.contains(file)])>0:
            #print(file + ' already exists in df')
            continue
        file_name = os.path.join(dir, file)
        graph = load_graph(model_file)
        t = read_tensor_from_image_file(file_name,input_height=input_height,input_width=input_width,input_mean=input_mean,input_std=input_std)
        input_name = "import/" + input_layer
        output_name = "import/" + output_layer
        input_operation = graph.get_operation_by_name(input_name)
        output_operation = graph.get_operation_by_name(output_name)
        with tf.Session(graph=graph) as sess:
            results = sess.run(output_operation.outputs[0],
                  {input_operation.outputs[0]: t})
        results = np.squeeze(results)
        top_k = results.argsort()[-5:][::-1]
        labels = load_labels(label_file)
        image = Image.open( file_name)
        font_type = ImageFont.truetype('/home/mmann1123/Documents/Fonts/unifont-10.0.07.ttf',25)
        draw = ImageDraw.Draw(image)
        draw.text(xy =(50,50),text=labels[top_k[0]]+' '+np.array2string(results[top_k[0]]),fill=(255,255,255), font=font_type)
        #image.show()
        
        #store path class date
        file_name2 = os.path.splitext(file_name)[0]
        date_in = file_name2.split("Picapture_")[1]
        date_time = datetime.strptime(date_in, "%d_%m_%Y-%H:%M:%S")
        df = df.append({'Path': file_name, 'Date': date_time, 'Class': labels[top_k[0]], 'Prob': results[top_k[0]]}, ignore_index=True) 
        print(labels[top_k[0]], results[top_k[0]])


