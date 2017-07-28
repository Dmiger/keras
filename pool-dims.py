# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 17:06:02 2017

@author: Sony VAIO Pro
"""

from keras.models import Sequential
from keras.layers import MaxPooling2D

model = Sequential()
model.add(MaxPooling2D(pool_size=2, strides=3, input_shape=(100, 100, 15)))
model.summary() 