import tensorflow as tf
from pathlib import Path
import mlflow
import numpy as np
import mlflow.keras
from urllib.parse import urlparse
from KidneyDiseaseClassifier.entity.config_entity import EvaluationConfig
from KidneyDiseaseClassifier.utils.common import read_yaml, create_directories,save_json
from dotenv import load_dotenv
from mlflow.models.signature import infer_signature


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
        load_dotenv()

    
    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.testing_data,
            subset="validation",
            shuffle=True,
            **dataflow_kwargs
        )


    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    
    def log_into_mlflow(self):
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {"loss": self.score[0], "accuracy": self.score[1]}
            )
            # Prepare a sample input for signature inference
            sample_input = np.random.random((1, 224, 224, 3)).astype(np.float32)
            sample_output = self.model.predict(sample_input)
            
            # Infer the model signature
            signature = infer_signature(sample_input, sample_output)

            # Log the model with the signature
            mlflow.keras.log_model(self.model, "model", signature=signature, registered_model_name="cnn-model-for-kidney-disease-classification")
            