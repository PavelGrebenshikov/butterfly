from django.http import HttpResponse


class ExceptionToHttpResponse:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, _request, exception) -> HttpResponse | None:
        if hasattr(exception, "status_code"):
            return HttpResponse(status=exception.status_code)
