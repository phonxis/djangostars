from threading import local

from django.utils.deprecation import MiddlewareMixin

from .models import SavedRequest


_local_thread = local()


def get_current_user():
    return getattr(_local_thread, 'user', None)


class SaveRequestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """
            Get some request data for saving in DB
        """
        request_data = {
            "request_method": request.META.get('REQUEST_METHOD', ''),
            "http_host": request.META.get('HTTP_HOST', ''),
            "http_user_agent": request.META.get('HTTP_USER_AGENT', ''),
            "server_protocol": request.META.get('SERVER_PROTOCOL', ''),
            "tz": request.META.get('TZ', ''),
            "path_info": request.META.get('PATH_INFO', ''),
            "user": request.user.username or "Anonymous"
        }
        SavedRequest.objects.create(**request_data)


class SaveCurrentUser(MiddlewareMixin):
    def process_request(self, request):
        _local_thread.user = getattr(request, 'user', None)
