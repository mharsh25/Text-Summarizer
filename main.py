from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger
from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME01="Data Ingestion Stage"
try:
    logger.info(f">>>>Stage {STAGE_NAME01} started<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>Stage {STAGE_NAME01} completed<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME02="Data Validation Stage"
try:
    logger.info(f">>>>Stage {STAGE_NAME02} started<<<<")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>Stage {STAGE_NAME02} completed<<<<")
except Exception as e:
    logger.exception(e)
    raise e