import random
import time

from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from typing import Dict


@csrf_exempt
def analyze(request: HttpRequest) -> JsonResponse:
    if int(random.uniform(1, 10)) >= 2:
        # do something...
        time.sleep(int(random.uniform(1, 3)))
        data = make_success_reponse()
    else:
        data = make_error_reponse()

    return JsonResponse(
        data=data
    )


def make_success_reponse() -> Dict:
    return {
        'success': True,
        'message': 'success',
        'estimated_data': {
            'class': int(random.uniform(1, 10)),
            'confidence': random.uniform(0.3, 1),
        }
    }


def make_error_reponse() -> Dict:
    return {
        'success': False,
        'message': 'Error:E50012',
        'estimated_data': {}
    }
