from django.shortcuts import render, redirect

# from .models import Question

def index(request):
    return redirect('polls/1/')
    # question = Question.objects.first()
    # return redirect(question)
