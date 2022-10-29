import keras
from keras.models import load_model
#from keras.preprocessing import image
import numpy as np
import tensorflow as tf

model = load_model('cats_and_dogs_small_2.h5')


def img_input(img_path):

  img = tf.keras.preprocessing.image.load_img(img_path, target_size=(150, 150))
  img_tensor = tf.keras.preprocessing.image.img_to_array(img)
  img_tensor = np.expand_dims(img_tensor, axis=0)
  img_tensor /= 255.
  prediction = model.predict(img_tensor)
  pred = round(prediction[0][0],2)

  if prediction > 0.5:
    res = 'This is a dog with '+str(pred)+' possibility'
  else:
    res = 'This is a cat with '+str(round(1-pred,2))+' possibility'

  return res

