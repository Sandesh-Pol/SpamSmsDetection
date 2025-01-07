from django.shortcuts import render
from django.http import JsonResponse

from .main import predict_spam

def index_view(request):
    if request.method == 'POST':
        sms_input = request.POST.get('sms_input', '')
        
        is_spam = predict_spam(sms_input)

        response_data = {
            'is_spam': bool(is_spam),
            'message': 'SPAM Detected!' if is_spam else 'Not a SPAM.'
        }

        return JsonResponse(response_data)

    return render(request, 'index.html')
