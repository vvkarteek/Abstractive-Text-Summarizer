from Abstractive_Text_Summarizer.config.configuration import ConfigurationManager
from Abstractive_Text_Summarizer.components.model_evaluation import ModelEvaluation
from Abstractive_Text_Summarizer.logging import logger




class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.evaluate()