from django.urls import path
from .views import AnalyzeView, AiAnalysisLogList


urlpatterns = [
    path('analyze/', AnalyzeView.as_view(), name='analyze'),
    path('', AiAnalysisLogList.as_view(), name='list'),
]
