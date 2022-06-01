from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

# Get questions and display them
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


# Show specific question and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    count = Question.objects.count() # number of table rows
    index = list(Question.objects.values_list('id', flat=True)).index(question_id) + 1 # row index
    context = {
        'question': question,
        'index': index,
        'count': count }
    return render(request, 'polls/detail.html', context)


# Display thanks
def thanks(request):
    return render(request, 'polls/thanks.html')


# Vote for a question choice
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    next_question = None
    count = Question.objects.count() # number of table rows
    index = list(Question.objects.values_list('id', flat=True)).index(question_id) + 1 # row index
    try:
        next_question = Question.objects.filter(id__gt=question_id)[:1][0]
    except IndexError:
        # TODO: handle this error
        pass
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'index': index,
            'count': count,
            'error_message': "Du har inte valt något alternativ.",
        }
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        if next_question:
            return HttpResponseRedirect(reverse('polls:detail', args=(next_question.id,)))
        else:
            return HttpResponseRedirect(reverse('polls:thanks'))
