import sys
import os
from os import listdir
from os.path import isfile, join

train_dir = '/Users/Ruta/Developer/STAC/finetune_alexnet_with_tensorflow/all/train'
files = [f for f in listdir(train_dir) if isfile(join(train_dir, f))]
num_files = len(files)

train_txt = open("train.txt", "w")
val_txt = open("val.txt", "w")
test_txt = open("test.txt", "w")

for i in range(num_files):
    # Retrieve the file name and label
    fname = files[i]
    pieces = fname.split(".")
    label = "0" if (pieces[0]=="cat") else "1"

    # Add to train.txt
    if float(i+1)/num_files < 0.7:
        train_txt.write(train_dir + "/" + fname + " " + label + "\n")
    # Add to val.txt
    elif 0.7 < (float(i+1)/num_files) < 0.85:
        val_txt.write(train_dir + "/" + fname + " " + label + "\n")
    # Add to test.txt
    else:
        test_txt.write(train_dir + "/" + fname + " " + label + "\n")
