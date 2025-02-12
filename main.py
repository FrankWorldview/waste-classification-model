# Dependencies
import numpy as np
import keras
# from keras.preprocessing.image import load_img
from tensorflow.keras.utils import load_img
# from keras.preprocessing.image import img_to_array
from tensorflow.keras.utils import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import VGG16
import tensorflow as tf

UPLOAD_FOLDER = './static/'

# def predict(img_path):
def getPrediction(filename):
     model = tf.keras.models.load_model("./final_model_weights.hdf5")
     img = load_img(UPLOAD_FOLDER+filename, target_size=(180, 180))
     img = img_to_array(img)
     img = img / 255
     img = np.expand_dims(img,axis=0)
     # category = model.predict_classes(img)
     category = np.argmax(model.predict(img),axis=1)
     answer = category[0]
     probability = model.predict(img)
     probability_results = 0

     if answer == 1:
          answer = "Recyclable"
          probability_results = probability[0][1]
     else:
          answer = "Organic"
          probability_results = probability[0][0]

     answer = str(answer)
     probability_results=str(probability_results)

     values = [answer, probability_results, filename]
     return values[0], values[1], values[2]
