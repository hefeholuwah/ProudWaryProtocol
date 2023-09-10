from django.http import JsonResponse
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def get_info(request):
    if request.method == 'GET':
        # Get query parameters
        slack_name = request.GET.get('slack_name')
        track = request.GET.get('track')

        # Get the current day of the week
        current_day = datetime.now().strftime('%A')

        # Get the current UTC time with validation of +/-2 hours
        current_time_utc = datetime.utcnow() + timedelta(hours=2)

        # URLs for GitHub file and source code
        file_url = 'https://github.com/hefeholuwah/ProudWaryProtocol/blob/main/django_project/views.py'
        source_code_url = 'https://github.com/hefeholuwah/ProudWaryProtocol'

        # Construct the response JSON
        response_data = {
            'slack_name': slack_name,
            'current_day': current_day,
            'utc_time': current_time_utc.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'track': track,
            'github_file_url': file_url,
            'github_repo_url': source_code_url,
            'status': 'Success',
        }

        return JsonResponse(response_data)
    else:
        return HttpResponse(status=405)  # Method Not Allowed
