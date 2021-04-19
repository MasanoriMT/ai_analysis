import json
import urllib.request
from abc import ABCMeta, abstractmethod

from typing import Dict

from .entities import AiAnalysisLogEntity
from .models import AiAnalysisLog

ANALYZE_API_ENDPOINT = 'http://example.com/mock-up/analyze/'


class AbstractAiAnalysisLogRepository(metaclass=ABCMeta):
    @abstractmethod
    def call_analyze(self, image_path: str) -> Dict:
        pass

    @abstractmethod
    def save(self, ai_analysis_log: AiAnalysisLogEntity) -> None:
        pass


class AiAnalysisLogRepository(AbstractAiAnalysisLogRepository):
    def call_analyze(self, image_path: str) -> Dict:
        """
        画像分析API呼び出し

        Args:
             image_path: 分析対象画像ファイル名
        Returns:
            Dict: APIレスポンス
        """
        data = {'image_path': image_path, }
        headers = {'Content-Type': 'application/json', }

        req = urllib.request.Request(ANALYZE_API_ENDPOINT, json.dumps(data).encode(), headers)
        with urllib.request.urlopen(req) as res:
            return json.load(res)

    def save(self, ai_analysis_log: AiAnalysisLogEntity) -> None:
        """
        画像分析結果の保管

        Args:
             ai_analysis_log: 分析処理結果Entity
        """
        AiAnalysisLog.objects.create(
            image_path=ai_analysis_log.image_path,
            success=ai_analysis_log.success,
            message=ai_analysis_log.message,
            class_field=ai_analysis_log.class_field,
            confidence=ai_analysis_log.confidence,
            request_timestamp=ai_analysis_log.request_timestamp,
            response_timestamp=ai_analysis_log.response_timestamp,
        )
