from rest_framework.response import Response

def createResponse(success, status, data, message):

    response = {
        'success': success,
        'status': status,
        'data': data,
        'message': message
    }

    return Response(response, status=status)
