from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def welcome(request):
    return HttpResponse('Welcome to the Meeting Planner!')


def date(request):
    return HttpResponse('This page was served at ' + str(datetime.now()))


def about(request):
    return HttpResponse("I'm Ivan and I make courses for Stepik ")
