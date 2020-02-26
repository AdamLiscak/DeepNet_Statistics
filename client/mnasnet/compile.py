 
import numpy as np
from tensorflow.keras.applications.nasnet import NASNetMobile
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.preprocessing import image
import tensorflow as tf
import time
import os


model = NASNetMobile(weights="imagenet")

import tempfile
import zipfile
'''
_, new_pruned_keras_file = tempfile.mkstemp(".h5")
print("Saving pruned model to: ", new_pruned_keras_file)
tf.keras.models.save_model(model, new_pruned_keras_file, include_optimizer=False)

# Zip the .h5 model file
_, zip3 = tempfile.mkstemp(".zip")
with zipfile.ZipFile(zip3, "w", compression=zipfile.ZIP_DEFLATED) as f:
    f.write(new_pruned_keras_file)
print(
    "Size of the pruned model before compression: %.2f Mb"
    % (os.path.getsize(new_pruned_keras_file) / float(2 ** 20))
)
print(
    "Size of the pruned model after compression: %.2f Mb"
    % (os.path.getsize(zip3) / float(2 ** 20))
)
'''
from tensorflow.python.framework import dtypes
tflite_model_file = "model.tflite"
converter = tf.lite.TFLiteConverter.from_keras_model(model)
#converter.target_spec.supported_types = [dtypes.float]
#converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_LATENCY]
tflite_model = converter.convert()
with open(tflite_model_file, "wb") as f:
    f.write(tflite_model)
'''
img = image.load_img('../mobilenet/cat.jpg', target_size=(227, 227))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
start = time.time()
preds = model.predict(x)
elapsed = start-time.time()
print('Predicted:', decode_predictions(preds))
print('ellapsed:',elapsed)
'''
