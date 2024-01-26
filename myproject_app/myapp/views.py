from django.http import HttpResponse


def index(request):
    return HttpResponse("Привет!")


def about(request):
    return HttpResponse("About us")



