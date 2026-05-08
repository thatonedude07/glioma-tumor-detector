import warnings
warnings.filterwarnings('ignore')

import numpy as np
import matplotlib.pyplot as pit
import os
import math
import shutil
import glob

# Counting the number of images in the respective classes example( 0 = Brain Tumor and 1 - Healthy)
ROOT_DIR = "C:\\Users\\karst\\Documents\\VSCODE PROJECT\\VSCODE BRAIN TUMOR PROJECT\\Brain tumor training images"
number_of_images = {}

for dir in os.listdir(ROOT_DIR): 
    # This will edit the number_of_images dictionary and will add in a key and value
    # The key is going to be the folder name and the value will be the amount of images in the folder 
    number_of_images[dir] = len(os.listdir(os.path.join(ROOT_DIR, dir)))

print(number_of_images.items())

'''
We will split the ddadta so that 
70% will go to training,
15% will be validation,
and 15% will be for testing
'''

# We will create a train foldedr
'''
if not os.path.exists("./train"): #Checks if folder is maded
    os.mkdir("./train") # Makes if ddoesn't exist

    for dir in os.listdir(ROOT_DIR): # This will give both healthy and bad mir images
        os.makedirs("./train/"+dir) #makeddirs will make multiple folders to seperate the healthy andd brain tumor images
        
        
        What the code below is doing is
        it is going through the folder
        and is randomly picking images to generalize the model
        the size will 70% of the images to be used for training
        the minus 2 will just make sure that it won't have an error 
        if a value is missing, 
        

        for img in np.random.choice(a = os.listdir(os.path.join(ROOT_DIR, dir)),
                                     size = (math.floor(70/100*number_of_images[dir]-2)),
                                        replace=False):
            # now we will transfer from the original folder to the training folder
            O = os.path.join(ROOT_DIR, dir, img) # Path
            D = os.path.join("./train", dir)
            os.remove(O)
    else:
        print("The folder exists")

'''

# function version
def dataFolder(foldername, split):
    p = "C:\\Users\\karst\\Documents\\VSCODE PROJECT\\VSCODE BRAIN TUMOR PROJECT\\" + foldername
    print(p)
    # split must be in decimal form, example 20% = .2, 5% = .05, etc
    if not os.path.exists(p): #Checks if folder is already made
        os.mkdir(p) # Makes if ddoesn't exist

        for dir in os.listdir(ROOT_DIR): # This will give both healthy and bad mir images
            
            os.makedirs(p+"/"+dir) #makeddirs will make multiple folders to seperate the healthy andd brain tumor images
            for img in np.random.choice(a = os.listdir(os.path.join(ROOT_DIR, dir)), 
                                    size = (math.floor(split*number_of_images[dir]-5)),
                                    replace=False):
                # now we will transfer from the original folder to the training folder
                O = os.path.join(ROOT_DIR, dir, img) # Path
                D = os.path.join(p, dir)
                shutil.copy(O,D)
                os.remove(O)
        '''
        What the code below is doing is
        it is going through the folder
        and is randomly picking images to generalize the model
        the size will take whatever percent you want through split of the images to be used for training
        the minus 2 will just make sure that it won't have an error 
        if a value is missing, 
        '''

    else:
        print(f"The {foldername} file exists")

dataFolder("train", 0.7)
dataFolder("validation", 0.15)
dataFolder("test", .15)

print(number_of_images.items())


