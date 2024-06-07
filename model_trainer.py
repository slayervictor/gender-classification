# Importing all necessary libraries
import os
import sys
import traceback

from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K

with open('logs.log', "a") as log_file:
    old_stdout = sys.stdout
    sys.stdout = log_file

    try:
        print('hello')
        print('Successfully completed execution.')
    except:
        print(traceback.format_exc())
    finally:
        sys.stdout = old_stdout
        log_file.flush()

img_width, img_height = 178, 218
app_mode = os.getenv('AppMode', None)
if app_mode:
    dir_path = '/app/data'
    train_data_dir = os.path.join(dir_path, 'Training')
    validation_data_dir = os.path.join(dir_path, 'Validation')
else:
    dir_path = r'C:\Users\Lucas\Pictures\02461 Pictures'
    train_data_dir = r'%s\Training' % dir_path
    validation_data_dir = r'%s\Validation' % dir_path


def get_file_count(path):
    count = 0
    for root_dir, cur_dir, files in os.walk(path):
        count += len(files)
    return count


nb_train_samples = get_file_count(train_data_dir)
nb_validation_samples = get_file_count(validation_data_dir)
print(f'{nb_train_samples=}')
print(f'{nb_validation_samples=}')
epochs = 10
batch_size = 16

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

model = Sequential()
kernel_size = (3, 3)
model.add(Conv2D(32, kernel_size, input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, kernel_size))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, kernel_size))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

model.fit(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size
)

model.save('model_saved.h5')
model.save_weights('model_saved_weights.h5')
