from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import tensorflow as tf
import keras
from keras.models import load_model
import cv2
import numpy as np

app = Flask(__name__)

try:
    model = keras.models.load_model("model_hand.h5")
except:
    model = keras.models.load_model("model_hand.h5")

letters = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X', 24:'Y',25:'Z'}

@app.route('/upload')
def upload_file():
   return render_template('index.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      # return 'file uploaded successfully'

      img = cv2.imread(f.filename)
      img_copy = img.copy()

      img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      img = cv2.resize(img, (400,440))


      img_copy = cv2.GaussianBlur(img_copy, (7,7), 0)

      img_gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
      _, img_thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)

      img_final = cv2.resize(img_thresh, (28,28))
      img_final =np.reshape(img_final, (1,28,28,1))
      print(img_final)
      
      pred = model.predict(img_final)
      print(pred)
      img_pred = letters[np.argmax(model.predict(img_final))]
      return f"The letter is : {str(img_pred)}\n\n"


if __name__ == '__main__':
   app.run(debug = True)   






   

      
         











