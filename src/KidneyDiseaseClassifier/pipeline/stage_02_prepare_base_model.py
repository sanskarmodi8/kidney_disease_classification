from KidneyDiseaseClassifier.config.configuration import ConfigurationManager
from KidneyDiseaseClassifier.components.prepare_base_model import PrepareBaseModel
from KidneyDiseaseClassifier import logger


STAGE_NAME = "Prepare base model"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


    
if __name__ == '__main__':
    try:
        logger.info(f"\n\n >>>>>> stage {STAGE_NAME} started <<<<<<\n\n")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e