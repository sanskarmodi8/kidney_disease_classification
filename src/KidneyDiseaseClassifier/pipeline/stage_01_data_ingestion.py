from KidneyDiseaseClassifier.config.configuration import ConfigurationManager
from KidneyDiseaseClassifier.components.data_ingestion import DataIngestion
from KidneyDiseaseClassifier import logger

STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        data_ingestion.split_data()



if __name__ == '__main__':
    try:
        logger.info(f"\n\n >>>>>> stage {STAGE_NAME} started <<<<<<\n\n")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e