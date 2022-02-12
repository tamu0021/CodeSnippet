from django.http import HttpRequest, HttpResponse

def top(request):
    return HttpResponse(b"Hello World")