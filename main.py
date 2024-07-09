from KidneyDiseaseClassifier import logger
from KidneyDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from KidneyDiseaseClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from KidneyDiseaseClassifier.pipeline.stage_03_training_model import ModelTrainingPipeline
from KidneyDiseaseClassifier.pipeline.stage_04_evaluation import EvaluationPipeline
from dotenv import load_dotenv

load_dotenv() # load the env vars from .env file


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f"\n\n>>>>>> stage {STAGE_NAME} started <<<<<<\n\n") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
   logger.exception(e)
   raise e


STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"\n\n>>>>>> stage {STAGE_NAME} started <<<<<<\n\n")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
   logger.exception(e)
   raise e


STAGE_NAME = "Training"
try: 
   logger.info(f"\n\n>>>>>> stage {STAGE_NAME} started <<<<<<\n\n")
   model_trainer = ModelTrainingPipeline()
   model_trainer.main()
   logger.info(f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
   logger.exception(e)
   raise e



STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"\n\n>>>>>> stage {STAGE_NAME} started <<<<<<\n\n")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")

except Exception as e:
   logger.exception(e)
   raise e