from django.http import HttpResponse,Render


def index(request):
    return Render("http://youtube.com")
#("Hello, world. You're at the polls index.")