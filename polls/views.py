from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index")

def detail(request, question_id):
    return HttpResponse("You're lookingat question %s." % question_id)

def results(request, question_id):
    response = HttpResponse("You're looking at the results of question %s." % question_id)
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on quetion %s." % question_id)
