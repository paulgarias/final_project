from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import tensorflow as tf
import keras
from keras.models import load_model
import cv2
import numpy as np


app = Flask(__name__)

model = keras.models.load_model('model_hand.h5')

@app.route('/upload')
def upload_file():
   return render_template('index.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

      # # # Read from file and convert to tensor
      # img_tensor = keras.io.decode_image(filename)
      # results = model.predict(img_tensor)

        # Delete the file
      # os.remove(filename)
      return "The letter is : "+str(results)+"\n\n"

if __name__ == '__main__':
   app.run(debug = True)   


      img = 


      # #read image file string data
      # f = request.files['file'].read()
      # #convert string data to numpy array
      # npimg = numpy.fromstring(f, numpy.uint8)
      # # convert numpy array to image
      # img = cv2.imdecode(npimg, cv2.CV_LOAD_IMAGE_UNCHANGED)
         











