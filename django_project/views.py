from django.http import JsonResponse
from datetime import datetime, timedelta

def get_info(request):
    slack_name = "Ifeoluwa Adefioye"
    track = "BackendTrack"

    current_day = datetime.now().strftime('%A')

    current_time = datetime.utcnow() + timedelta(hours=2)  # Adjust for UTC+2

    file_url = 'https://github.com/hefeholuwah/ProudWaryProtocol/blob/main/django_project/views.py'
    source_code_url = 'https://github.com/hefeholuwah/ProudWaryProtocol'

    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'current_utc_time': current_time.strftime('%Y-%m-%d %H:%M:%S'),
        'track': track,
        'file_url': file_url,
        'source_code_url': source_code_url,
        'status': 'Success',
    }

    return JsonResponse(response_data)
