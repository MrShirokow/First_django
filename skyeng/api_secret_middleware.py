from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseForbidden
from config.settings import API_SECRET
from skyeng.internal import utils


class ApiSecretMiddleware:
    """
    Middleware checks that the API_SECRET from the request matches the secret from setting.py
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        if request.headers.get('X-Signature') != utils.get_signature(request, API_SECRET):
            return HttpResponseForbidden('Unknown API key')
        return self.get_response(request)
