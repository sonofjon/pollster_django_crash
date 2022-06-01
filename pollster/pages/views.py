from django.shortcuts import render, redirect

from polls.models import Question

def index(request):
    # return redirect('polls/1/')
    id = Question.objects.first().id
    return redirect('polls/' + str(id))
