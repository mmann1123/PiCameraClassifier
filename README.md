# PiCameraClassifier

## Description
This project aims to utilize a rasberry pi 3 to calculate the frequency of truck and buses on the street outside my house. Since we live near a FedEx distribution center I am particularly interested in counting the number fedex delivery trucks on my street.

![Setup and taking pictures](https://github.com/mmann1123/PiCameraClassifier/raw/master/Readme/IMG_20171118_1139332.jpg)

Although I am just getting started it seems very easy to retrain a tensorflow deep learning algorithm through transfer learning, and uploading that model to the rasberry pi. See instructions [here](https://svds.com/tensorflow-image-recognition-raspberry-pi/) and tensorflow retraining [here](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0). Additional training images can be found in Imagenet [here](http://www.image-net.org/synset?wnid=n03173929#) and from the rasberry pi camera feed,  

I started with the Adafruit Rasberry pi 3 camera kit, although it's much cheaper to buy through Arrow.com [here](https://www.arrow.com/en/products/3275/adafruit-industries). Full kit for 88$ plus free next day shipping (at least to DC)! Camera setup instructions can be found [here](https://learn.adafruit.com/diy-wifi-raspberry-pi-touch-cam)


## Sample of out-of-sample testing
![Testing/car2.jpeg](https://github.com/mmann1123/PiCameraClassifier/raw/master/Readme/car2.jpeg)

```
python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=Testing/car2.jpeg

2017-11-18 12:12:59.255913: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX

notafedextruck 0.999974
fedextruck 2.60127e-05
```
