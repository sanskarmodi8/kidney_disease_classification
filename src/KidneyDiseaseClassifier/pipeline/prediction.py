import numpy as np
import tensorflow as tf
import os
import mlflow
import mlflow.pyfunc

image = tf.keras.preprocessing.image
load_model = tf.keras.models.load_model

class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename
        os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/sanskarmodi8/kidney_disease_classification.mlflow"

    
    def predict(self):
        
        # use mlflow registered model 
        model_name="cnn-model-for-kidney-disease-classification"
        model_version = 1
        model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{model_version}")
        
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        print(result)

        if result[0] == 0:
            prediction = 'Cyst'
            return [{ "image" : prediction}]
        elif result[0] == 1:
            prediction = 'Normal'
            return [{ "image" : prediction}]
        elif result[0] == 2:
            prediction = 'Stone'
            return [{ "image" : prediction}]
        elif result[0] == 3:
            prediction = 'Tumor'
            return [{ "image" : prediction}]
        else:
            prediction = 'Unknown'
            return [{ "image" : prediction}]
