# run following in shell
#cd ~/Documents/tensorflow-for-poets-2/
#source activate tensorflow   # activate anaconda environment with tensorflow
IMAGE_SIZE=224
ARCHITECTURE="mobilenet_1.0_${IMAGE_SIZE}"
python -m scripts.retrain   --bottleneck_dir=tf_files/bottlenecks    --model_dir=tf_files/models/   --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}"   --output_graph=tf_files/retrained_graph.pb   --output_labels=tf_files/retrained_labels.txt      --image_dir=/home/mmann1123/Dropbox/PiCapture/StreetCapture --random_brightness=5  --architecture="${ARCHITECTURE}" --how_many_training_steps=2000

#removign architecture flag with default to inception v3 

# run from python
import scripts.label_image
import sys
import numpy as np
import tensorflow as tf

def load_graph(model_file):
  graph = tf.Graph()
  graph_def = tf.GraphDef()
  with open(model_file, "rb") as f:
    graph_def.ParseFromString(f.read())
  with graph.as_default():
    tf.import_graph_def(graph_def)
  return graph


def read_tensor_from_image_file(file_name, input_height=299, input_width=299,
				input_mean=0, input_std=255):
  input_name = "file_reader"
  output_name = "normalized"
  file_reader = tf.read_file(file_name, input_name)
  if file_name.endswith(".png"):
    image_reader = tf.image.decode_png(file_reader, channels = 3,
                                       name='png_reader')
  elif file_name.endswith(".gif"):
    image_reader = tf.squeeze(tf.image.decode_gif(file_reader,
                                                  name='gif_reader'))
  elif file_name.endswith(".bmp"):
    image_reader = tf.image.decode_bmp(file_reader, name='bmp_reader')
  else:
    image_reader = tf.image.decode_jpeg(file_reader, channels = 3,
                                        name='jpeg_reader')
  float_caster = tf.cast(image_reader, tf.float32)
  dims_expander = tf.expand_dims(float_caster, 0);
  resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
  normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
  sess = tf.Session()
  result = sess.run(normalized)
  return result

def load_labels(label_file):
  label = []
  proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
  for l in proto_as_ascii_lines:
    label.append(l.rstrip())
  return label


input_height = 224
input_width = 224
input_mean = 128
input_std = 128
input_layer = "input"
output_layer = "final_result"
label_file = r'/home/mmann1123/Documents/PiCameraClassifier/tf_files/retrained_labels.txt'
model_file = r'/home/mmann1123/Documents/PiCameraClassifier/tf_files/retrained_graph.pb'
 

###############################
# iterate across series of photos 
import os
from PIL import Image, ImageDraw, ImageFont
import time
import psutil
os.chdir(r'/home/mmann1123/Dropbox/Apps/PiCameraLogger/14_03_2018/')
rootdir = os.getcwd()

for dir, dirs, files in os.walk(rootdir):
    for file in files:
    	file_name = os.path.join(dir, file)
	print(file_name)
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
	print(labels[top_k[0]], results[top_k[0]])
	image = Image.open( file_name)
	font_type = ImageFont.truetype('/home/mmann1123/Documents/Fonts/unifont-10.0.07.ttf',25)
	draw = ImageDraw.Draw(image)
	draw.text(xy =(50,50),text=labels[top_k[0]]+' '+np.array2string(results[top_k[0]]),fill=(255,255,255), font=font_type)
	image.show()
	time.sleep(5)
	# hide image
	for proc in psutil.process_iter():
		if proc.name() == "display":
			proc.kill()
 



################## single photo 

# path to file to classify 
file_name = r'/home/mmann1123/Dropbox/PiCapture/Testing/Fedex.jpg'

graph = load_graph(model_file)
t = read_tensor_from_image_file(file_name,
                          input_height=input_height,
                          input_width=input_width,
                          input_mean=input_mean,
                          input_std=input_std)

input_name = "import/" + input_layer
output_name = "import/" + output_layer
input_operation = graph.get_operation_by_name(input_name);
output_operation = graph.get_operation_by_name(output_name);

with tf.Session(graph=graph) as sess:
   results = sess.run(output_operation.outputs[0],
              {input_operation.outputs[0]: t})


results = np.squeeze(results)


top_k = results.argsort()[-5:][::-1]
labels = load_labels(label_file)
for i in top_k:
  print(labels[i], results[i])

# print most likely label 
print(labels[top_k[0]], results[top_k[0]])



