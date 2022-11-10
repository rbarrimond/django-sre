import json
import logging

from django.utils import timezone
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Retrieve the Django logger
logger = logging.getLogger('django')

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    logger.debug('Enter')

    status = {}
    status['module'] = __name__
    status['value'] = 'OK'
    status['path'] = request.path

    logger.info(json.dumps(status))
    
    logger.debug('Exit')
    return HttpResponse(json.dumps(status))
