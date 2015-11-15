from django.shortcuts import render, get_object_or_404
from django.template import loader, RequestContext
from django.http import HttpResponse, Http404

from polls.models import Question


# Lists all the questions in a list
def questions(request):
    # Grab all the questions from the Model Questions
    question_list = Question.objects.all()

    # Get the template that we need, which is questions.html
    template = loader.get_template('questions.html')

    # Create context to return with template in a HTTPResponse
    context = RequestContext(request, {
        'question_list': question_list,
    })

    # Returns the HTTPResponse with a template that has the context in it
    return HttpResponse(template.render(context))


# Shows the specific text and choices for a question
def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    #
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist.')

    return render(request, 'detail.html', {'question': question})

