from .models import *
from datetime import datetime
class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        return response
    def process_template_response(self, request, response):

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        url = request.get_full_path()
        moment = datetime.now()
        Refresh.objects.get_or_create(url=url, ip=ip, datetime=moment)

        time_t = moment.replace(minute=moment.minute-1)
        refreshes = Refresh.objects.filter(datetime__gte=time_t)
        refresh_count = len(refreshes)
        print moment
        response.context_data["refresh"] = refresh_count

        # Code to be executed for each request/response after
        # the view is called.
        return response
