import os

import numpy as np
from keras.models import load_model
from keras.utils import load_img

dir_path = r'C:\Users\Lucas\Pictures\02461 Pictures\AI_Test'
model = load_model(r'trained_models/model_saved_6400x1600_e22.h5')
male_folder_name = 'male'
female_folder_name = 'female'

# Create folders to sort images into.
for name in [male_folder_name, female_folder_name]:
    path = os.path.join(dir_path, name)
    if not os.path.exists(path):
        os.makedirs(path)

for path in os.listdir(dir_path):
    # check if current path is a file
    join = os.path.join(dir_path, path)
    if os.path.isfile(join):
        image = load_img(join, target_size=(178, 218))
        img = np.array(image)
        img = img / 255.0
        img = img.reshape(1, 178, 218, 3)
        label = model.predict(img)
        print("Predicted Class (0 - female , 1- male): ", label[0][0], join)
        if label[0][0] < 0.5:
            sub = female_folder_name
        else:
            sub = male_folder_name
        # print(join)
        li = os.path.split(join)
        joined_pa = os.path.join(li[0], sub, li[1])
        # print(joined_pa)
        os.rename(join, joined_pa)
