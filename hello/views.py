from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import Greeting
import hello.addadvice as addadvice

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    times = int(os.environ.get('TIMES', 3))
    # return HttpResponse('Hello!' * times)
    return render(request, "index.html")

def twitterAPI(request):
    return HttpResponse(addadvice.Advice('test').addAdvice())




def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
