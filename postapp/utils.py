from django.http import JsonResponse

def api_response(code, message, data=None):
    return JsonResponse({
        'code': code,
        'message': message,
        'data': data
    })
    


