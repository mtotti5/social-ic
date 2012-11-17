from django.http import HttpResponse
from django.shortcuts import render_to_response

def login(request):
    return render_to_response('login.html', {"foo": "bar"})


def place(request,loc):
    return HttpResponse(nickname)