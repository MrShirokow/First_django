import base64
import hashlib
import hmac
import io

from django.db.models import QuerySet
from django.http import HttpRequest, QueryDict


def get_signature(request: HttpRequest, key: str):
    request_str = f'{request.method}\n{request.path}'
    return hmac.new(key.encode(), request_str.encode(), hashlib.sha256).hexdigest()


def positive_int(integer_string: str, strict=False, cutoff=None):
    number = int(integer_string)
    if number < 0 or (number == 0 and strict):
        raise ValueError()
    if cutoff:
        return min(number, cutoff)
    return number


def get_limit(query_params: QueryDict, default: int = 50):
    try:
        return positive_int(query_params.get('limit'),
                            strict=True,
                            cutoff=100)
    except (TypeError, ValueError):
        return default


def get_offset(query_params: QueryDict):
    try:
        return positive_int(query_params.get('offset'))
    except (TypeError, ValueError):
        return 0


def paginate(query_params: QueryDict, query_set: QuerySet):
    offset = get_offset(query_params)
    limit = get_limit(query_params)
    return query_set[offset:offset + limit]


def decode_file(encoded_data: str):
    return io.BytesIO(base64.b64decode(encoded_data.encode('utf-8')))
