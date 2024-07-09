from KidneyDiseaseClassifier.config.configuration import ConfigurationManager
from KidneyDiseaseClassifier.components.evaluation import Evaluation
from KidneyDiseaseClassifier import logger



STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()




if __name__ == '__main__':
    try:
        logger.info(f"\n\n >>>>>> stage {STAGE_NAME} started <<<<<<\n\n")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f"\n\n>>>>>> stage {STAGE_NAME} completed <<<<<<\n\n")
    except Exception as e:
        logger.exception(e)
        raise e
            