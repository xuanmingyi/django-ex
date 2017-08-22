from django.http import HttpResponse


def index(request):
    return HttpResponse("dafasf")

def health(request):
    return HttpResponse("7")
