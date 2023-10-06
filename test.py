import numpy as np # numpy arrays are very fast and can perform large computations in a very short time
import pandas as pd # helps to load the data frame in a 2D array format
import matplotlib.pyplot as plt # used to draw visializations
import seaborn as sb # also used to draw visializations

from glob import glob
from PIL import Image
from sklearn.model_selection import train_test_split # used to split the data into training and testing

import tensorflow as tf
from tensorflow import keras
from keras import layers
from functools import partial

AUTO = tf.data.experimental.AUTOTUNE
import warnings
warnings.filterwarnings('ignore')

images = glob('train_cancer/*/*.jpg')
print(len(images))

