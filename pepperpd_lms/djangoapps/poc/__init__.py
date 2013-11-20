from django.http import HttpResponse


def view(request):
    return HttpResponse("I believe this proves the concept.")
