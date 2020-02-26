import tensorflow as tf
import numpy as np
import keras
from keras.applications.mobilenet_v2 import MobileNetV2
from keras.datasets import cifar10
from keras.preprocessing import image
from keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
#import matplotlib.pyplot as plt
#import cv2
import time
(x_train, y_train), (x_test, y_test) = cifar10.load_data()
img_path = "cat.jpg"
img = image.load_img(img_path, target_size=(224, 224))
#plt.imshow(img)
img = image.img_to_array(img)
#plt.show()
model = MobileNetV2(weights='imagenet')
img = preprocess_input(img)
img = np.expand_dims(img, axis=0)
start = time.time()
preds = model.predict(img)
elapsed = time.time()-start
print(preds.argmax(axis=1))
print(elapsed)

# decode the results into a list of tuples (class, description, probability)
# (one such list for each sample in the batch)
print('Predicted:', decode_predictions(preds, top=3)[0])
