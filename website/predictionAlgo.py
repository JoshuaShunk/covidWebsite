from flask import Blueprint, render_template, request, flash, session, current_app, abort, send_from_directory, redirect, url_for
from keras.models import load_model
import cv2
import os
import numpy as np 
import matplotlib.pyplot as plt

def predict():
    
    model = load_model('website\static\Best_VGG16CNP.h5')

    catigories = ['Covid 19 Pneumonia', 'Normal', 'Viral Pneumonia']
    filePath = session.get('filePath')
    fileName = session.get('fileName')
    path = 'website/static/uploads/'

    imgPath2 = os.path.join(path, fileName)

    img = cv2.imread(imgPath2)
    img = cv2.resize(img,(128,128))

    img = np.reshape(img,[1,128,128,3])
    img = img/255

    pred = np.argmax(model.predict(img), axis=-1)

    predictedCondition = catigories[int(pred)]
    print(predictedCondition)

    return predictedCondition