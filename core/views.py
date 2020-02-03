from django.http import JsonResponse
import requests
import base64
import json
from uuid import uuid4
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def subir_imagen(request):
    if request.method == 'POST':
        img = request.FILES['imagen']
        img_str = base64.b64encode(img.read()).decode('utf-8')
        ext = img.content_type.replace('image/', '.')

        # print(img_str)

        res = requests.post(
            'https://n5w29niyjj.execute-api.us-east-1.amazonaws.com/testing',
            json=json.dumps({
                'body': img_str,
                'filename': f'{uuid4()}{ext}'
            })
        )

        return JsonResponse(res.json())

    return JsonResponse({
        'status': 400,
        'message': 'SOLO HACER PETICIONES AL METODO POST!!!'
    })
