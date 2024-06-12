from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import datetime

@api_view(['GET'])
def get_current_time(request):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return JsonResponse({'time': current_time}, status=status.HTTP_200_OK)


# Create a new function GET hello?key=World
# that returns a JSON {"message": "Hello World"} when the query parameter key is present
# and return HTTP 501 code with message "key query parameter is required"
# when the query parameter key is not present
@api_view(['GET'])
def get_hello(request):
    key = request.GET.get('key')
    if key:
        return JsonResponse({'message': f'Hello {key}'}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'message': 'key query parameter is required'}, status=status.HTTP_501_NOT_IMPLEMENTED)
        


