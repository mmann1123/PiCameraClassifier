# PiCameraClassifier

## Description
This project aims to utilize a rasberry pi 3 to calculate the frequency of truck and buses on the street outside my house. Since we live near a FedEx distribution center I am particularly interested in counting the number fedex delivery trucks on my street.

![Setup and taking pictures](https://github.com/mmann1123/PiCameraClassifier/raw/master/Readme/IMG_20171118_1139332.jpg)

Although I am just getting started it seems very easy to retrain a tensorflow deep learning algorithm through transfer learning, and uploading that model to the rasberry pi. See instructions [here](https://svds.com/tensorflow-image-recognition-raspberry-pi/) and tensorflow retraining [here](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0). Additional training images can be found in Imagenet [here](http://www.image-net.org/synset?wnid=n03173929#) and from the rasberry pi camera feed,  

I started with the Adafruit Rasberry pi 3 camera kit, although it's much cheaper to buy through Arrow.com [here](https://www.arrow.com/en/products/3275/adafruit-industries). Full kit for 88$ plus free next day shipping (at least to DC)! Camera setup instructions can be found [here](https://learn.adafruit.com/diy-wifi-raspberry-pi-touch-cam)

## A quick training test
```
cd ~/Documents/tensorflow-for-poets-2/
source activate tensorflow   # activate anaconda environment with tensorflow

IMAGE_SIZE=224
ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"

# retrain 
python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps=500 \
  --model_dir=tf_files/models/ \
  --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --architecture="${ARCHITECTURE}" \
  --image_dir=RetrainingPhotos
```

## Examples from out-of-sample testing
These are a first pass at retraining the classifier using about 30 examples of fedex trucks and other trucks/cars and only 500 training steps. 

![Testing/car2.jpeg](https://github.com/mmann1123/PiCameraClassifier/raw/master/Readme/car2.jpeg)

```
python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=Testing/car2.jpeg

2017-11-18 12:12:59.255913: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX

notafedextruck 0.999974
fedextruck 2.60127e-05
```

![Testing/fedex2.jpeg](https://github.com/mmann1123/PiCameraClassifier/raw/master/Readme/fedex2.jpeg)
```
python -m scripts.label_image     --graph=tf_files/retrained_graph.pb      --image=Testing/fedex2.jpeg
2017-11-18 12:27:00.936555: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX

fedextruck 1.0
notafedextruck 9.88756e-11
```

![Testing/whitetruck.jpeg](https://github.com/mmann1123/PiCameraClassifier/raw/master/Readme/whitetruck.jpeg)
``` 
python -m scripts.label_image     --graph=tf_files/retrained_graph.pb      --image=Testing/whitetruck.jpeg
2017-11-18 12:28:09.792163: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX
fedextruck 0.999915
notafedextruck 8.54759e-05
```

 

