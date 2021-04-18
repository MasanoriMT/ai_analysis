from django.db import models


class AiAnalysisLog(models.Model):
    image_path = models.CharField(max_length=255, blank=True, null=True)
    success = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    class_field = models.IntegerField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    confidence = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    request_timestamp = models.PositiveIntegerField(blank=True, null=True)
    response_timestamp = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'ai_analysis_log'
