from rest_framework.response import Response

from common.err_code import my_error_code
from djpro import settings


def success_response(data=''):
    """
    :param data: 
    :return: 
    """
    return Response(data={'code': 0, 'msg': '成功', 'data': data})


def error_response(reason, data=''):
    """
    :param reason: key of my_error_code in error_code.py
    :param data: 
    :return: 
    """
    return Response(data={'code': reason[0], 'msg': reason[1], 'data': data})


def serializer_error_reason(serializer):
    """
    the error reason of serializer.is_valid() is not True
    use for debug
    :param serializer: 
    :return: 
    """
    reason = [k + ':' + v[0] for k, v in serializer.errors.items()]
    return reason


def serializer_error(serializer):
    """
    response differentiate developer or production
    :param serializer: 
    :return: 
    """
    if settings.DEBUG:
        return serializer_error_reason(serializer)
    return error_response(my_error_code['SERIALIZER_ERROR'])