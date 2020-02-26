
import numpy as np
import tensorflow as tf
import time
import sys
from keras.preprocessing import image
import glob
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="aaa",
  database="statistics_convnet"
)
mycursor = mydb.cursor()

sql1 = "INSERT INTO statistics(time) values(%s)"
sql2 = "INSERT INTO results(probability,guess_column,stat_id) values(%s,%s,%s)"
sql3 = "SELECT COUNT(id) from statistics"

mycursor.execute(sql3)
interpreter = tf.lite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
content = []
with open("../val_mapping_minimal.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
img = []
filenames = glob.glob("../val_img/*.JPEG")
filenames.sort()
m = mycursor.fetchall()[0][0]


for i in filenames:
   # print(i)
    img = image.load_img(i, target_size=(224, 224))
    img = image.img_to_array(img)
    img = img.astype(np.float32)

    input_shape = input_details[0]['shape']
    input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], [img])
    start = time.time()
    interpreter.invoke()
    end = time.time()-start
    endtuple = (end,)

    mycursor.execute(sql1, endtuple)

    output_data = interpreter.get_tensor(output_details[0]['index'])
    results = -np.sort(-output_data)[0][:5]
    columns = np.argpartition(output_data[0], -5)[-5:]
    columns = columns[np.argsort(-output_data[0][columns])]
    print(columns)
    for r in range(len(results)):
        rtuple = (float(results[r]),int(columns[r]),m+1)
        mycursor.execute(sql2,rtuple)
          
    print(output_data.argmax(axis=1))
  #  print(m)
    print(end)
    m+=1

mydb.commit()

#print(img)
#'../mobilenet/cat.jpg'
# Load TFLite model and allocate tensors.


# Get input and output tensors.


# Test model on random input data.


# The function `get_tensor()` returns a copy of the tensor data.
# Use `tensor()` in order to get a pointer to the tensor.

