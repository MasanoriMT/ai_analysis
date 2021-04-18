from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, FormView

from .services import (
    AnalyzeService,
)

from .models import AiAnalysisLog


class AnalyzeView(FormView):
    """
    画像分析実行画面
    """

    template_name = 'analyze.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        画面表示
        """
        return render(request, self.template_name)

    def post(self, request: HttpRequest) -> HttpResponse:
        """
        画像分析を実行する
        """
        analyze_service = AnalyzeService()
        image_path = request.POST.get('image_path')
        result = analyze_service.analyze(
            image_path=image_path
        )
        if result:
            messages.success(request, 'Analysis successful.')
        else:
            messages.error(request, 'Analysis failed.')

        return render(request, self.template_name)


class AiAnalysisLogList(ListView):
    """
    画像分析結果確認画面
    """
    template_name = 'list.html'
    model = AiAnalysisLog
