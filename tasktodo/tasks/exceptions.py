from rest_framework.exceptions import APIException

class AccessItemException(APIException):
    status_code = 401
    default_detail = 'You are not allowed to access the item'
    default_code = 'unauthorized'
