# RaspberryPi testing scripts
## How does it work ?
A remote device with keras and tensorflow logs in to a database on a remote server, establishes
a direct connection  and starts insert test values into the database....


these include : top-5 results, measurement time

## where is what ?

### client

There are multiple directories which contain the following files:
compile.py... compiles the keras model to a model.tflite
Launcher.py ... launches the model.tflite
<parent_directory_name>.py ... keras implementation of the model with no compilation

### server

The server contains utilities for initializing the ILSVRC2012 validation ground truth on the database, sql commands for analysing the database and a log with records of indices that have
to be written manually.

It also contains a directory "graphing" which contains methods for aggregating measurement times with relative frequencies directly... in effect creating those graphs which look
like gaussians. grapher.py is a product of wrong thought, it calculates a strange mutant
of the integral and the original function.

grapher_deriv is the function that calculates those curves seen in my work.

mobilenetDiscrepancy evalutes the integral of the 170-195ms cluster for linearity.

serialize.py downloads all records from the database to a json file

###  Json file

the values collected by my measurement exceed 50 mb, the json file itself has 72 mb  therefore it is compressed as databasedump.tar.gz

could have just gone with a database 

### indices of models
tests have been done on the following neural networks:
each test takes 50 000 values, hence every neural network can be seen as a block of 
50 000 ids 

1 squeezenet_tflite
50001 mobilenetV2_tflite
100001 mobilenetv1_tfite
150001 nasnet_mobile_tflite
200001 mobilenetv1_tfite





