from src.textsummarizer.config.configuration import ConfigurationManager
from src.textsummarizer.components.data_validation import DataValidation
from src.textsummarizer.logging import logger





class DataValidationTrainingPipeline:
    def __init_(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.download_file()
        data_validation.extract_zip_file()