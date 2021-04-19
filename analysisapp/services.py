import time

from .repositories import AbstractAiAnalysisLogRepository
from .entities import AiAnalysisLogEntity


class AnalyzeService:
    def __init__(self, repository:AbstractAiAnalysisLogRepository):
        self.__ai_analysis_log_repository = repository

    def analyze(self, image_path: str) -> bool:
        """
        画像分析を実行する

        Args:
             image_path: 分析対象画像ファイル名
        Returns:
            bool: 分析処理が成功したか
        """
        try:
            ai_analysis_log_entity = self.process(image_path)
            if ai_analysis_log_entity is None:
                return False

            self.__ai_analysis_log_repository.save(ai_analysis_log_entity)
        except:
            return False

        return True

    def process(self, image_path: str) -> AiAnalysisLogEntity:
        """
        画像分析処理

        Args:
             image_path: 分析対象画像ファイル名
        Returns:
            AiAnalysisLogEntity: 分析処理結果Entity
        """
        ai_analysis_log_entity = AiAnalysisLogEntity()
        ai_analysis_log_entity.image_path = image_path
        ai_analysis_log_entity.request_timestamp = int(time.time())

        response = self.__ai_analysis_log_repository.call_analyze(image_path)
        if not response['success']:
            return None

        ai_analysis_log_entity.success = response['success']
        ai_analysis_log_entity.message = response['message']
        ai_analysis_log_entity.class_field = response['estimated_data']['class']
        ai_analysis_log_entity.confidence = response['estimated_data']['confidence']
        ai_analysis_log_entity.response_timestamp = int(time.time())

        return ai_analysis_log_entity
