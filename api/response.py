from rest_framework.response import Response

class Response(Response):
    def __init__(self, data=None, status=None, message=None, template_name=None, headers=None, exception=False, content_type=None):
        if type(data) == str: message = data
        data = {
            'status': status,
            'message': message if message else '',
            'data': data if type(data) in [dict, list] else {},
        }
        super().__init__(data, status, template_name, headers, exception, content_type)