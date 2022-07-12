import base64
import functools
import hashlib
import hmac
import io

from django.http import HttpResponseForbidden
from config.settings import API_SECRET


def api_secret_check(request_function):

    @functools.wraps(request_function)
    def request_wrapper(self, request, *args, **kwargs):
        if request.headers.get('X-Signature') != get_signature(request, API_SECRET):
            return HttpResponseForbidden('Unknown API key')
        return request_function(self, request, *args, **kwargs)

    return request_wrapper


def get_signature(request, key):
    request_str = f'{request.method}\n{request.path}'
    return hmac.new(key.encode(), request_str.encode(), hashlib.sha256).hexdigest()


def positive_int(integer_string, strict=False, cutoff=None):
    number = int(integer_string)
    if number < 0 or (number == 0 and strict):
        raise ValueError()
    if cutoff:
        return min(number, cutoff)
    return number


def get_limit(query_params, default=50):
    try:
        return positive_int(query_params.get('limit'),
                            strict=True,
                            cutoff=100)
    except (TypeError, ValueError):
        return default


def get_offset(query_params):
    try:
        return positive_int(query_params.get('offset'))
    except (TypeError, ValueError):
        return 0


def paginate(query_params, query_set):
    offset = get_offset(query_params)
    limit = get_limit(query_params)
    return query_set[offset:offset + limit]


def decode_file(encoded_data: str):
    return io.BytesIO(base64.b64decode(encoded_data.encode('utf-8')))
